import json
import logging
from json import JSONDecodeError
from urllib.parse import parse_qs, urlparse

import allure
import curlify
import requests
from allure_commons.types import AttachmentType
from requests import Session, Response


def raise_for_status(response: requests.Response):
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        if response.status_code == 400:
            e.add_note(response.text)
            raise


def allure_attach_request(function):
    """Декоратор логироваания запроса, хедеров запроса, хедеров ответа в allure шаг и аллюр аттачмент и в консоль."""
    def wrapper(*args, **kwargs):
        method, url = args[1], args[2]
        with allure.step(f"{method} {url}"):

            response: Response = function(*args, **kwargs)

            curl = curlify.to_curl(response.request)
            logging.debug(curl)
            logging.debug(response.text)

            allure.attach(
                body=curlify.to_curl(curl).encode("utf8"),
                name=f"Request {response.status_code}",
                attachment_type=AttachmentType.TEXT,
                extension=".txt"
            )
            try:
                allure.attach(
                    body=json.dumps(response.json(), indent=4).encode("utf8"),
                    name=f"Response json {response.status_code}",
                    attachment_type=AttachmentType.JSON,
                    extension=".json"
                )
            except JSONDecodeError:
                allure.attach(
                    body=response.text.encode("utf8"),
                    name=f"Response text {response.status_code}",
                    attachment_type=AttachmentType.TEXT,
                    extension=".txt")
            allure.attach(
                body=json.dumps(response.headers, indent=4).encode("utf8"),
                name=f"Response headers {response.status_code}",
                attachment_type=AttachmentType.JSON,
                extension=".json"
            )
        raise_for_status(response)
        return response

    return wrapper


class BaseSession(Session):
    """Сессия с прокидыванием base_url и логированием запроса, ответа, хедеров ответа."""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.base_url = kwargs.pop("base_url", "")

    @allure_attach_request
    def request(self, method, url, **kwargs):
        """Логирование запроса и вклейка base_url."""
        return super().request(method, self.base_url + url, **kwargs)


class AuthSession(Session):
    """Сессия с прокидыванием base_url и логированием запроса, ответа, хедеров ответа.
    + Автосохранение cookies внутри сессии из кааждого response и redirect response, и 'code'."""
    def __init__(self, *args, **kwargs):
        """
        Прокидываем base_url - url авторизации из энвов
        code - код авторизации из redirect_uri"""
        super().__init__()
        self.base_url = kwargs.pop("base_url", "")
        self.code = None

    @allure_attach_request
    def request(self, method, url, **kwargs):
        """Сохраняем все cookies из redirect'a и сохраняем code авторизации из redirect_uri,
        И используем в дальнейшем в последующих запросах этой сессии."""
        response = super().request(method, self.base_url + url, **kwargs)
        for r in response.history:
            cookies = r.cookies.get_dict()
            self.cookies.update(cookies)
            code = parse_qs(urlparse(r.headers.get("Location")).query).get("code", None)
            if code:
                self.code = code
        return response

from requests import Session


class ApiClient:
    def __init__(self, base_url: str, token: str):
        """
        Инициализатор сессии
        :param base_url: Базовый урл
        :param token: Bearer token
        """
        self.base_url = base_url
        self.session = Session()
        self.session.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }


class ApiCategories(ApiClient):
    def __init__(self, base_url: str, token: str):
        super().__init__(base_url, token)

    def get_category_list(self):
        """
        Получаем все категории
        :return: category list
        """
        response = self.session.get(f'{self.base_url}/api/categories/all')
        response.raise_for_status()
        return response.json()

    def add_category(self, category_name: str):
        """
        Добавляем категорию
        :param category_name: Имя добавляемой категории
        :return: success 200, id = hash, username = кто создал категорию, category = название категории
        """
        response = self.session.post(f'{self.base_url}/api/categories/add', json={
            'category': category_name
        })
        response.raise_for_status()
        return response.json()


class ApiProfile(ApiClient):
    def __init__(self, base_url: str, token: str):
        super().__init__(base_url, token)

    def update_profile(self, firstname: str, currency: str, photo, surname: str):
        """
        Меняем значения в профиле
        :param firstname: любое значение
        :param currency: str EUR, RUB, KZT, USD
        :param photo: optional
        :param surname: любое значение
        :return:
        """
        response = self.session.post(f'{self.base_url}api/users/update', json={
            'currency': currency,
            'firstname': firstname,
            'photo': photo,
            'surname': surname
        })
        response.raise_for_status()
        return response.json()


class ApiSpends(ApiClient):
    def __init__(self, base_url: str, token: str):
        super().__init__(base_url, token)

    def get_spends_list(self):
        """
        Получаем список трат
        :return:
        """
        response = self.session.get(f'{self.base_url}/api/spends/all')
        response.raise_for_status()
        return response.json()

    def add_spend(self, category: str, amount: float, currency: str, description: str, spend_date: str):
        """
        Добавляем трату
        :param category: str любое значение
        :param amount: float значение
        :param currency: str EUR, RUB, KZT, USD
        :param description: str любое значение
        :param spend_date:
        :return:    "id": "36a13409-485e-46e3-bb80-50cd3202a813",
                    "spendDate": "2024-09-15T06:26:56.984+00:00",
                    "category": "for",
                    "currency": "EUR",
                    "amount": 4.0,
                    "description": "qa-guru",
                    "username": "pavelqa"
        """
        response = self.session.post(f'{self.base_url}/api/spends/add', json={
            'category': category,
            'amount': amount,
            'description': description,
            'spendDate': spend_date,
            'currency': currency,
        })
        response.raise_for_status()
        return response.json()

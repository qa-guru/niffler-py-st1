from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, HttpUrl
import requests
from fastapi.responses import JSONResponse
import uvicorn

class User(BaseModel):
    id: int
    email: EmailStr | None = Field(default=None)
    first_name: str
    last_name: str
    avatar: HttpUrl | None = Field(default=None)


class UsersResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]
    support: dict


class UserResponse(BaseModel):
    data: User
    support: dict


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UpdateUserRequest(BaseModel):
    name: str
    job: str


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: str


class DeleteUserResponse(BaseModel):
    delete: int


app = FastAPI()


@app.get("/users")
async def get_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    users_response = UsersResponse(**response.json())
    return users_response.model_dump()



@app.get("/users/{user_id}")
async def get_user(user_id: int):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    user_response = UserResponse(**response.json())
    return user_response.model_dump()


@app.post("/users")
async def create_user(user: CreateUserRequest):
    response = requests.post("https://reqres.in/api/users", json=user.model_dump())
    create_user_response = CreateUserResponse(**response.json())
    return create_user_response.model_dump()


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UpdateUserRequest):
    response = requests.put(f"https://reqres.in/api/users/{user_id}", json=user.model_dump())
    update_user_response = UpdateUserResponse(**response.json())
    return update_user_response.model_dump()


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    response = requests.delete(f"https://reqres.in/api/users/{user_id}")
    delete_user_response = DeleteUserResponse(**response.json())
    return delete_user_response.model_dump()

if __name__ == "__service__":
    uvicorn.run(app)
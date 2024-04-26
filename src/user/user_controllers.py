from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from . import user_resolvers
from models import UserResponse

router = APIRouter()

# Контроллер для создания нового пользователя
@router.post("/user")
async def create_user(request: CreateUserRequest):
    user = await user_resolvers.create_user(
        request.name, request.addr, request.sign)
    return UserResponse(**user)

# Контроллер для обновления данных пользователя
@router.put("/user/{id}")
async def update_user(id: int, request: UpdateUserRequest):
    user = await user_resolvers.update_user(
        id, request.name, request.desc, request.description, request.cover, request.image)
    if user:
        return UserResponse(**user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Контроллер для удаления пользователя
@router.delete("/user/{id}")
async def delete_user(id: int):
    user = await user_resolvers.delete_user(id)
    if user:
        return UserResponse(**user)
    else:
        raise HTTPException(status_code=404, detail="User not found")


# Контроллер для получения пользователя по его id
@router.get("/getUser/{id}", response_model=UserResponse)
async def get_user(id: int):
    user = await user_resolvers.get_user(id)
    if user:
        return UserResponse(**user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Контроллер для получения всех пользователей
@router.get("/allUsers", response_model=List[UserResponse])
async def get_users():
    users = await user_resolvers.get_users()
    return [UserResponse(**user) for user in users]

# Экспорт роутера
__all__ = ["router"]




"""from user_resolvers import create_user, get_user_by_id, update_user

# Контроллеры для обработки запросов от фронтенда
async def create_user_controller(name: str, email: str):
    try:
        # Вызываем функцию из модели для создания нового пользователя
        new_user = await create_user(name, email)
        return new_user
    except Exception as e:
        # Обработка ошибок, если возникнет ошибка при создании пользователя
        raise Exception("Failed to create user: {}".format(str(e)))


async def get_user_controller(user_id):
    try:

    except Exception as e:
        raise Exception("Failed to get user: {}".format(str(e)))

async def update_user_controller(user_id, data):
    try:

    except Exception as e:
        raise Exception("Failed to update user: {}".format(str(e)))


from user_resolvers import resolve_user, ….

Def handle_create_transaction (....):
"""



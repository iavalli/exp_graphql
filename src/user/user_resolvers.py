"""
from models import User, Balance, Tx

# Подключение к MongoDB - проверить код
MONGO_URI = "mongodb://localhost:27017"
mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client["your_database"]
users_collection = db["users"]

Функции для выполнения запросов к базе данных

@strawberry.field
def users() -> List[User]:
    return users_collection


async def get_user_by_id(id):


async def create_user(addr, sign):


async def update_user(id, name, ):
"""

from fastapi import FastAPI, HTTPException
from bson import ObjectId
from main import users_collection
from models import User, Balance, Tx, Contact


# Резолверы для объекта User
async def get_user(id: int):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def get_users():
    users = []
    async for user in users_collection.find():
        users.append(user)
    return users


async def get_all_user_contacts(id: int):
    user = await users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user.get("contacts", [])
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def create_user(name: str, addr: str, sign: str):
    user_data = {"name": name, "addr": addr, "sign": sign}
    result = await users_collection.insert_one(user_data)
    user_data["_id"] = result.inserted_id
    return user_data


async def update_user(id: int, name: str, desc: str, description: str, cover: str, image: str):
    update_data = {}
    if name:
        update_data["name"] = name
    if desc:
        update_data["desc"] = desc
    if description:
        update_data["description"] = description
    if cover:
        update_data["cover"] = cover
    if image:
        update_data["image"] = image

    await users_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    updated_user = await users_collection.find_one({"_id": ObjectId(id)})
    return updated_user


async def delete_user(id: int):
    deleted_user = await users_collection.find_one({"_id": ObjectId(id)})
    if deleted_user:
        await users_collection.delete_one({"_id": ObjectId(id)})
        return deleted_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Регистрация резолверов в FastAPI
@app.get("/getUser/{id}", response_model=User)
async def get_user(id: int):
    return await get_user(id)

@app.get("/allUsers", response_model=List[User])
async def get_users():
    return await get_users()

@app.get("/user/{id}/contacts", response_model=List[Contact])
async def get_user_contacts(id: int):
    return await all_user_contacts(id)

@app.post("/user")
async def create_user(name: str, addr: str, sign: str):
    return await create_user(name, addr, sign)

@app.put("/user/{id}")
async def update_user(id: int, name: str = None, desc: str = None, description: str = None, cover: str = None, image: str = None):
    return await update_user(id, name, desc, description, cover, image)

@app.delete("/user/{id}")
async def delete_user(id: int):
    return await delete_user(id)

from typing import List
import strawberry
from strawberry.asgi import GraphQL
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from schema import schema


# Подключение к MongoDB - проверить код
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mydatabase"]
users_collection = db["users"]


schema = strawberry.Schema(query=type('Query', (object,), {
    'users': users,
    'balances': balances,
    'transactions': transactions,
}), mutation=type('Mutation', (object,), {
    'create_user': create_user,
}))


app = FastAPI()

@app.post("/graphql")
async def graphql(request: Request):
    response = await GraphQL(schema)(request)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
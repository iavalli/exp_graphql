"""
import strawberry
from user_controllers import create_user_controller, get_user_controller
from user_controllers import update_user_controller

@strawberry.type
class User:
    id: strawberry.ID
    name: str
    email: str


@strawberry.type
class Query:
    ...


@strawberry.mutation
async def create_user(name: str, email: str) -> User:
    user = User(id=str(uuid.uuid4()), name=name, email=email)
    result = await users_collection.insert_one(user.dict())
    return user


@strawberry.type
class Mutation:
    create_user: User
    update_user: User

schema = strawberry.Schema(query=Query, mutation=Mutation)
"""

type User {
    id: ID!
    addr: String!
    name: String
    cover: String
    image: String
    desc: String
    description: String
    sign: String!
    balance: Balance!
    contacts:[Contact!]!
}

type Contact {
    id: ID!
    name: String!
    image:
    description: String 
}

type Query {
    getUser(id: ID!): User!
    getUsers: [User!]! # getUsers или allUsers?
    allUserContacts(id: ID!): [Contact!]
}

type Mutation {
    createUser(name: String!, addr: String!, sign: String!): User!
    updateUser(id: ID!, name: String, desc: String, description: String, cover: String, image: String): User!
    deleteUser(id: ID!): User
}

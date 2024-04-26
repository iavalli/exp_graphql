from pydantic import (BaseMoodel, PositiveInt)


class User(BaseModel):
    id: int
    addr: str
    name: Optional[str]
    cover: Optional[str]
    image: Optional[str]
    desc: Optional[str]
    description: Optional[str]
    sign: str
    balance: int


class Balance(BaseModel):
    # balanceid: userid
    addr: str
    balanceamount: int


class Tx(BaseModel):
    txid: int
    uniq: str
    credit: str
    debit: str
    amount: PositiveInt
    time: Optional[int]
    sign: str
    hash: Optional[str]
    prev_hash: Optional[str]
    msg: Optional[str]


class Contact:
    id: int
    name: Optional[str]
    image: Optional[str]
    description: Optional[str]


# Модель данных для создания нового пользователя
class CreateUserRequest(BaseModel):
    name: str
    addr: str
    sign: str

# Модель данных для обновления пользователя
class UpdateUserRequest(BaseModel):
    name: str
    desc: str = None
    description: str = None
    cover: str = None
    image: str = None

# Модель данных для ответа с пользователем
class UserResponse(BaseModel):
    id: int
    addr: str
    name: str
    cover: str = None
    image: str = None
    desc: str = None
    description: str = None
    sign: str
    balance: int

"""@strawberry.type
class Transaction:
    id: strawberry.ID
    user_id: strawberry.ID
    amount: float
    description: str
"""

"""
credit - адрес отправителя
debit - адрес получателя
"""

type Tx {
    id: ID!
    credit: String!
    debit: String!
    amount: Int!
    sign: String!
    hash: String
    msg: String
    message: String
    time: Int
    """
    created_at:
    sender: {
        id: ID!
        name:
    }
    recipient: {
        id: ID!
        name:
    }
    """
}


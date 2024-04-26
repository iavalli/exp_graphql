
"""@strawberry.type
class Balance:
    user_id: strawberry.ID
    amount: float
"""
type Balance {
    owner: User!
    addr: String!
    amount: Int!
    txs: [Tx]
}

type Query {
    getBalance($id): Balance!
    getallBalances: [Balance!]!
}

type Mutation {
    createBalance(owner: User!): Balance!
    updateBalance(owner: User!): Balance!
    deleteBalance(owner: User!): Balance!
}

type Subscription {
    newBalance(owner: User!): Balance!
    updatedBalance(owner: User!): Balance!
    deletedBalance(owner: User!): Balance!
}

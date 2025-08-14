class AccountModel:

    def __init__(self, id: str, balance: float = 0.0):
        self.id = id
        self.balance = balance

    def __repr__(self):
        return str(self.__dict__)

    def to_dict(self):
        return {"id": self.id, "balance": self.balance}

    @classmethod
    def get(cls, id: str):
        return account_objects.get(id)

    @classmethod
    def deposit(cls, id: str, balance: float):
        if id not in account_objects:
            account_objects[id] = AccountModel(id)

        account_objects[id].balance += balance
        return account_objects[id]

    def withdraw(self, balance: float):
        self.balance -= balance
        return self


account_objects = dict[str, AccountModel]()

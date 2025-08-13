accounts = {}


class AccountModel:
    objects = accounts

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def __repr__(self):
        return str(self.__dict__)

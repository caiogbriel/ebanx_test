from models.Account import AccountModel


def reset_accounts():
    AccountModel.delete_all()

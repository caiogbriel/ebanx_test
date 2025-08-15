from models.Account import AccountModel


def reset_accounts():
    AccountModel.delete_all()


def get_account_balance(account_id: str):
    account = AccountModel.get(account_id)

    return account.balance if account else None

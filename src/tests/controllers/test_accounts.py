from unittest import TestCase
from unittest.mock import Mock, patch

from controllers.accounts import get_account_balance, reset_accounts


class TestResetAccounts(TestCase):
    @patch("controllers.accounts.AccountModel")
    def test_reset_accounts_calls_delete_all(self, mock_account_model):
        reset_accounts()
        mock_account_model.delete_all.assert_called_once()


class TestGetAccountBalance(TestCase):
    @patch("controllers.accounts.AccountModel")
    def test_get_account_balance_existing_account(self, mock_account_model):
        mock_account = Mock()
        mock_account.balance = 100.0
        mock_account_model.get.return_value = mock_account

        result = get_account_balance("123")

        assert result == 100.0
        mock_account_model.get.assert_called_once_with("123")

    @patch("controllers.accounts.AccountModel")
    def test_get_account_balance_nonexistent_account(self, mock_account_model):
        mock_account_model.get.return_value = None

        result = get_account_balance("999")

        assert result is None
        mock_account_model.get.assert_called_once_with("999")

    @patch("controllers.accounts.AccountModel")
    def test_get_account_balance_zero_balance(self, mock_account_model):
        mock_account = Mock()
        mock_account.balance = 0
        mock_account_model.get.return_value = mock_account

        result = get_account_balance("456")

        assert result == 0
        mock_account_model.get.assert_called_once_with("456")

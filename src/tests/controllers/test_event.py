from unittest import TestCase
from unittest.mock import Mock, patch

from controllers.event import manage_event
from controllers.interfaces.event import (
    DepositData,
    EventType,
    TransferData,
    WithdrawData,
)
from models.Account import AccountModel


class TestManageEvent(TestCase):
    @patch.object(AccountModel, "deposit")
    def test_deposit_creates_new_account(self, mock_deposit):
        mock_account = Mock()
        mock_account.to_dict.return_value = {"id": "100", "balance": 10}
        mock_deposit.return_value = mock_account

        result = manage_event(
            EventType.DEPOSIT, DepositData(destination="100", amount=10)
        )

        mock_deposit.assert_called_once_with("100", 10)
        assert result == {"destination": {"id": "100", "balance": 10}}

    @patch.object(AccountModel, "get")
    def test_withdraw_from_existing_account(self, mock_get):
        mock_account = Mock()
        mock_account.to_dict.return_value = {"id": "100", "balance": 15}
        mock_get.return_value = mock_account

        result = manage_event(
            EventType.WITHDRAW, WithdrawData(origin="100", amount=5)
        )

        mock_get.assert_called_once_with("100")
        mock_account.withdraw.assert_called_once_with(5)
        assert result == {"origin": {"id": "100", "balance": 15}}

    @patch.object(AccountModel, "get")
    def test_withdraw_from_nonexistent_account_returns_none(self, mock_get):
        mock_get.return_value = None

        result = manage_event(
            EventType.WITHDRAW, WithdrawData(origin="200", amount=10)
        )

        assert result is None

    @patch.object(AccountModel, "get")
    @patch.object(AccountModel, "deposit")
    def test_transfer_between_accounts(self, mock_deposit, mock_get):
        # Setup withdraw
        mock_origin_account = Mock()
        mock_origin_account.to_dict.return_value = {
            "id": "100",
            "balance": 0,
        }
        mock_get.return_value = mock_origin_account

        # Setup deposit
        mock_dest_account = Mock()
        mock_dest_account.to_dict.return_value = {
            "id": "300",
            "balance": 15,
        }
        mock_deposit.return_value = mock_dest_account

        result = manage_event(
            EventType.TRANSFER,
            TransferData(origin="100", destination="300", amount=15),
        )

        assert result == {
            "origin": {"id": "100", "balance": 0},
            "destination": {"id": "300", "balance": 15},
        }

    @patch.object(AccountModel, "deposit")
    def test_deposit_event_type_is_handled(self, mock_deposit):
        mock_account = Mock()
        mock_account.to_dict.return_value = {"id": "100", "balance": 10}
        mock_deposit.return_value = mock_account

        result = manage_event(
            EventType.DEPOSIT, DepositData(destination="100", amount=10)
        )

        assert result is not None

    @patch.object(AccountModel, "get")
    def test_withdraw_event_type_is_handled(self, mock_get):
        mock_account = Mock()
        mock_account.to_dict.return_value = {"id": "100", "balance": 10}
        mock_get.return_value = mock_account

        result = manage_event(
            EventType.WITHDRAW, WithdrawData(origin="100", amount=5)
        )

        assert result is not None

    @patch.object(AccountModel, "get")
    @patch.object(AccountModel, "deposit")
    def test_transfer_event_type_is_handled(self, mock_deposit, mock_get):
        mock_account = Mock()
        mock_account.to_dict.return_value = {"id": "100", "balance": 10}
        mock_get.return_value = mock_account
        mock_deposit.return_value = mock_account

        result = manage_event(
            EventType.TRANSFER,
            TransferData(origin="100", destination="300", amount=15),
        )

        assert result is not None

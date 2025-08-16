import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


class TestBalanceAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch("views.balance.get_account_balance")
    def test_get_balance_existing_account(self, mock_get_balance):
        mock_get_balance.return_value = 20.0

        response = self.client.get("/balance?account_id=100")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "20.0")
        mock_get_balance.assert_called_once_with("100")

    @patch("views.balance.get_account_balance")
    def test_get_balance_nonexistent_account(self, mock_get_balance):
        mock_get_balance.return_value = None

        response = self.client.get("/balance?account_id=999")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, "0")
        mock_get_balance.assert_called_once_with("999")

    @patch("views.balance.get_account_balance")
    def test_get_balance_zero_balance(self, mock_get_balance):
        mock_get_balance.return_value = 0.0

        response = self.client.get("/balance?account_id=200")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "0.0")
        mock_get_balance.assert_called_once_with("200")

    def test_get_balance_missing_account_id(self):
        response = self.client.get("/balance")

        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()

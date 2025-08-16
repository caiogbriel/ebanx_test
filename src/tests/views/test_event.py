import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


class TestEventAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch("views.event.manage_event")
    def test_deposit_event_success(self, mock_manage_event):
        mock_manage_event.return_value = {
            "destination": {"id": "100", "balance": 10}
        }

        payload = {"type": "deposit", "destination": "100", "amount": 10}
        response = self.client.post("/event", json=payload)

        self.assertEqual(response.status_code, 201)

        expected = {"destination": {"id": "100", "balance": 10}}
        self.assertEqual(response.json(), expected)

    @patch("views.event.manage_event")
    def test_withdraw_event_success(self, mock_manage_event):
        mock_manage_event.return_value = {
            "origin": {"id": "100", "balance": 15}
        }

        payload = {"type": "withdraw", "origin": "100", "amount": 5}
        response = self.client.post("/event", json=payload)

        self.assertEqual(response.status_code, 201)
        expected = {"origin": {"id": "100", "balance": 15}}
        self.assertEqual(response.json(), expected)

    @patch("views.event.manage_event")
    def test_withdraw_from_non_existing_account(self, mock_manage_event):
        mock_manage_event.return_value = None

        payload = {"type": "withdraw", "origin": "999", "amount": 10}
        response = self.client.post("/event", json=payload)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, "0")

    @patch("views.event.manage_event")
    def test_transfer_event_success(self, mock_manage_event):
        mock_manage_event.return_value = {
            "origin": {"id": "100", "balance": 0},
            "destination": {"id": "300", "balance": 15},
        }

        payload = {
            "type": "transfer",
            "origin": "100",
            "destination": "300",
            "amount": 15,
        }
        response = self.client.post("/event", json=payload)

        self.assertEqual(response.status_code, 201)
        expected = {
            "origin": {"id": "100", "balance": 0},
            "destination": {"id": "300", "balance": 15},
        }
        self.assertEqual(response.json(), expected)

    @patch("views.event.manage_event")
    def test_transfer_from_non_existing_account(self, mock_manage_event):
        mock_manage_event.return_value = None

        payload = {"type": "transfer", "origin": "999", "destination": "100", "amount": 10}
        response = self.client.post("/event", json=payload)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, "0")


if __name__ == "__main__":
    unittest.main()

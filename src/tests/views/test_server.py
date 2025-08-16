import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


class TestServerAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch("views.server.reset_accounts")
    def test_reset_endpoint_idempotent_success(self, mock_reset):
        response1 = self.client.post("/reset")
        response2 = self.client.post("/reset")

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.text, "OK")

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.text, "OK")

        self.assertEqual(mock_reset.call_count, 2)

    def test_reset_endpoint_wrong_method(self):
        response = self.client.get("/reset")

        self.assertEqual(response.status_code, 405)


if __name__ == "__main__":
    unittest.main()

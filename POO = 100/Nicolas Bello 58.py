import unittest
from unittest.mock import patch, Mock
from service_to_test import UserService
import requests

class TestUserService(unittest.TestCase):
    @patch('service_to_test.requests.get')
    def test_get_user_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "John Doe", "email": "john@example.com"}
        mock_get.return_value = mock_response

        user_service = UserService()
        data = user_service.get_user_data(1)
        self.assertEqual(data["name"], "John Doe")
        mock_get.assert_called_once_with("https://api.example.com/users/1")

    @patch('service_to_test.requests.get')
    def test_get_user_data_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        user_service = UserService()
        with self.assertRaises(requests.exceptions.HTTPError):
            user_service.get_user_data(999)
        mock_get.assert_called_once_with("https://api.example.com/users/999")

if __name__ == '__main__':
    unittest.main()

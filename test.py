import pytest
import unittest
from unittest.mock import patch
from main import lambda_handler


# class Test(unittest.TestCase):
#     @patch('main.load_s3_file', return_value=['Kayky', 'Guilherme'])
#     def test_lambda_handler(self, load_s3_file):
#         response = lambda_handler(None, None)
#         self.assertEqual(response, 'Kayky, Guilherme, ')

@patch('main.load_s3_file', return_value=['Kayky', 'Guilherme'])
def test_lambda_handler(load_s3_file):
    response = lambda_handler(None, None)
    assert response == 'Kayky, Guilherme, '


if __name__ == '__main__':
    # unittest.main()
    pytest.main()

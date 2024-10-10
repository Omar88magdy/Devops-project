import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello from Dockerized Flask app!')

if __name__ == '__main__':
    unittest.main()

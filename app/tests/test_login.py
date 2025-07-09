import unittest
from app.dao import auth_user


class TestLogin(unittest.TestCase):
    def test_login_success(self):
        self.assertTrue(auth_user('nhathung', '123456'))


    def test_login_failure(self):
        self.assertFalse(auth_user('admin', 'wrongpassword'))


if __name__ == '__main__':
    unittest.main()


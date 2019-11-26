import unittest
from user import User

class UserTestCase(unittest.TestCase):

    def test_valid_user(self):

        temp_user = User("test@gmail.com", "test", "test", 22)

        self.assertTrue(temp_user.is_valid())

    def test_under_age(self):

        temp_user = User("test@gmail.com", "test", "test", 12)

        self.assertFalse(temp_user.is_valid())

    def test_above_age(self):

        temp_user = User("test@gmail.com", "test", "test", 14)

        self.assertTrue(temp_user.is_valid())

    def test_invalid_email(self):

        temp_user = User("testgmail.com", "test", "test", 14)

        self.assertFalse(temp_user.is_valid())

    def test_invalid_first_name(self):

        temp_user = User("test@gmail.com", "", "test", 14)

        self.assertFalse(temp_user.is_valid())

    def test_invalid_last_name(self):

        temp_user = User("test@gmail.com", "test", "", 14)

        self.assertFalse(temp_user.is_valid())



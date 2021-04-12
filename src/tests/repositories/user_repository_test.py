import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_amanda = User('Amanda', 'a', 0)

    def test_creation(self):
        user_repository.create(self.user_amanda)
        all_users = user_repository.find_all()
        
        self.assertEqual(all_users[0].username, self.user_amanda.username)
        self.assertEqual(len(all_users), 1)

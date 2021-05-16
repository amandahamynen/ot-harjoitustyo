import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_amanda = User('Amanda', 'a', 'a', 'a')
        self.user_toinen = User('Toinen', 't', 't', 't')
        self.user_kolmas = User('Kolmas', 'k', 'k', 'k')

    def test_creation(self):
        user_repository.create(self.user_amanda)
        all_users = user_repository.find_all()

        self.assertEqual(all_users[0].username, self.user_amanda.username)
        self.assertEqual(len(all_users), 1)

    def test_find_by_username(self):
        user_repository.create(self.user_toinen)
        user = user_repository.find_by_username(self.user_toinen.username)
        self.assertEqual(user.username, self.user_toinen.username)

    def test_find_all(self):
        user_repository.create(self.user_amanda)
        user_repository.create(self.user_toinen)
        user_repository.create(self.user_kolmas)
        users = user_repository.find_all()

        self.assertEqual(users[0].username, self.user_amanda.username)
        self.assertEqual(users[1].username, self.user_toinen.username)
        self.assertEqual(users[2].username, self.user_kolmas.username)

        self.assertEqual(len(users), 3)

    def test_delete_all(self):
        user_repository.create(self.user_amanda)
        user_repository.create(self.user_toinen)
        
        users = user_repository.find_all()
        self.assertEqual(len(users), 2)

        user_repository.delete_all()
        users = user_repository.find_all()
        self.assertEqual(len(users), 0)

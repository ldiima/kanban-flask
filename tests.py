import os
import unittest

from app import app, db, Todo

TEST_DB = 'tests.db'

class BasicTests(unittest.TestCase):

    # execute before each test 
    # set up 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # teardown
    def tearDown(self):
        pass

#TESTS
    # check index page route
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # check new task add function
    def test_add_todo(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # check task delete function
    def test_delete_todo(self):
        response = self.app.get('/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

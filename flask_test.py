import os
import orderingsys
import unittest
import tempfile
from orderingsys import app

class orderingsysTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, orderingsys.app.config['DATABASE'] = tempfile.mkstemp()
        orderingsys.app.config['TESTING'] = True
        self.app = orderingsys.app.test_client()
        orderingsys.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(orderingsys.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

if __name__ == '__main__':
    unittest.main()
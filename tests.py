from flaskr import app
import unittest


class FlaskrTestCase(unittest.TestCase): 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def test_empty_db(self):
        """Start with a blank database."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200) 
        assert b'No entries here so far' in response.data

    def test_login_logout(self):
        """Make sure login and logout works"""
        response = self.app.post('/login', data=dict(
            username='admin', password='default'), follow_redirects=True)
        assert b'You were logged in' in response.data
        response = self.app.get('/logout', follow_redirects=True)
        assert b'You were logged out' in response.data
        response = self.app.post('/login', data=dict(
            username='admin2', password='default'), follow_redirects=True)
        assert b'Invalid username' in response.data
        response = self.app.post('/login', data=dict(
            username='admin', password='default2'), follow_redirects=True)
        assert b'Invalid password' in response.data

    def test_messages(self):
        """Test that messages work"""
        self.app.post('/login', data=dict(
            username='admin', password='default'), follow_redirects=True)
        response = self.app.post('/add', data=dict(
            title='<Hello>', text='<strong>HTML</strong> allowed here'), 
            follow_redirects=True)
        assert b'No entries here so far' not in response.data
        assert b'&lt;Hello&gt;' in response.data
        assert b'<strong>HTML</strong> allowed here' in response.data


if __name__ == '__main__':
    unittest.main()

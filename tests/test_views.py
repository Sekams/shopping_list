import os
import unittest
from app import app
from app.views import the_application


class FlaskTestCase(unittest.TestCase):
    """Test cases for the application views"""

    def setUp(self):
        """This method initializes the varibles of the tests"""
        self.tester = app.test_client(self)
        app.secret_key = os.urandom(12)
        the_application.signup("Homer", "Simpson", "homie", "duff")

    def test_index(self):
        """This method tests if the route / returns 200"""
        response = self.tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        """This method tests if the route /signup returns 200"""
        response = self.tester.post("/signup", data=dict(first_name="Marge", last_name="Simpson",
                                                         username="marge_s", password="maggie"),
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

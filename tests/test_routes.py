import unittest
from webapp.app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        """
        Set up Flask app for testing
        """
        app.testing = True
        self.client = app.test_client()

    def test_homepage_no_session(self):
        """
        When given the index URL without session,
        we should return a 302 status code redirection
        """

        self.assertEqual(self.client.get("/").status_code, 302)

    def test_not_found(self):
        """
        When given a non-existent URL,
        we should return a 404 status code
        """

        self.assertEqual(self.client.get("/not-found-url").status_code, 404)


if __name__ == "__main__":
    unittest.main()

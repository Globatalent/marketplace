from test_plus.test import TestCase

from marketplace.campaigns.helpers import generate_token_code


class TestUser(TestCase):

    def test_generate_token_code(self):
        self.assertEqual("SNT", generate_token_code("Some name Foo"))
        self.assertEqual("NNT", generate_token_code("Name"))
        self.assertEqual("TTT", generate_token_code(""))


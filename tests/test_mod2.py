from unittest import TestCase
from packages.mod2.main import foo

class Test(TestCase):

    def test_foo_bar(self):
        foo()
        self.assertEqual(1, 1)
        print("worked")
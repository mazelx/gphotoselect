import unittest
from core.api import gpFinder


class TestGpFinder (unittest.TestCase):
    def setUp(self):
        self.gpf = gpFinder()

    def test_exists(self):
        self.assertEquals(self.gpf.exists("P4090819"), True)

    def test_not_exists(self):
        self.assertEquals(self.gpf.exists("P1234567"), False)


if __name__ == '__main__':
    unittest.main()

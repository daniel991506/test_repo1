import unittest
from mymath import add, sub, multi, devide
class testmath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)

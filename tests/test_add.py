import unittest
from add_numbers import add

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


assert add(1, 2) == 3
print("Assertion passed!")

if __name__ == '__main__':
    unittest.main()
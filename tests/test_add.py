import unittest
from add_numbers import add, subtract

import sys
import os

# Add the parent directory of the current file to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



assert add(1, 2) == 3
print("Add function assertion passed!")


assert subtract(5, 3) == 2
print("Subtract function assertion passed!")


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, -1), 0)




if __name__ == '__main__':
    

    unittest.main()

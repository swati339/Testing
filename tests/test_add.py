# import unittest
import pytest
from add_numbers import add, subtract

import sys
import os

# Add the parent directory of the current file to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@pytest.mark.addition
def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

@pytest.mark.subtraction
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

assert add(1, 2) == 3
print("Add function assertion passed!")


assert subtract(5, 3) == 2
print("Subtract function assertion passed!")


# class TestAddFunction(unittest.TestCase):
# def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(0, 0), 0)

# def test_subtract(self):
#         self.assertEqual(subtract(5, 3), 2)
#         self.assertEqual(subtract(3, 5), -2)
#         self.assertEqual(subtract(0, 0), 0)
#         self.assertEqual(subtract(-1, -1), 0)




# if __name__ == '__main__':
    

    # unittest.main()

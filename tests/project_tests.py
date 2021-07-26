import unittest

from main import *

class TestProjectCode(unittest.TestCase):
    def test_numbers(self):
        assert(add_numbers(1, 4) == 5)
        assert (add_numbers(-1, 4) == 3)


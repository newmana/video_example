import unittest

from main import *

class TestProjectCode(unittest.TestCase):
    def test_numbers(self):
        assert(add_numbers(1, 4) == 5)

    def test_negative_add(self):
        assert (add_numbers(-1, 4) == 3)


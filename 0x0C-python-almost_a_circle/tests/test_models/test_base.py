#!/usr/bin/python3
"""Test cases for the Base Class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to test different cases for Base Class"""

    def case_for_positive_and_negative(self):
        """Test for both +ve and -ve id numbers"""

        ins = Base(400)
        self.assertEqual(ins.id, 400)

        ins = Base(-50)
        self.assertEqual(ins.id, -50)

    def case_for_none_and_nothingPassed(self):
        """Testing for none"""

        ins = Base()
        self.assertEqual(ins.id, 1)

        ins = Base()
        self.assertEqual(ins.id, 2)

        ins = Base()
        self.assertEqual(ins.id, 3)

        ins = Base(None)
        self.assertEqual(ins.id, 4)

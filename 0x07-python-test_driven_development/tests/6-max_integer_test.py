#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ this is test cases for the 6-max_integer
    function"""

    def test_maxint(self):
        self.assertEqual(max_integer([50, 30, 101, 0, 77]), 101)

    def float(self):
        self.assertEqual(max_integer([6.6, 7.6, 405, 505.5]), 505.5)

    def empty(self):
        self.assertEqual(max_integer([]))

    def negnum(self):
        self.assertEqual(max_integer([-8, -10, -1, -55]), -1)

    def samenum(self):
        self.assertEqual(max_integer([-5, -5, -5, -5, -5]), -5)

    def oprs(self):
        self.assertEqual(max_integer([10 / 10, 40 + 50, 400, 50 * 4,
        4000 - 3999]), 400)

    def lotsofNums(self):
        self.assertEqual(max_integer([2939232, 8398974, 3239238938, 9283989,
            198299, 3, 4 / 4, 0, 9, 90000000, 490, 54050, 94, 49, 34,
            434, 545, 3232, 311, 33231, 3435, 78787, 6656, 5454]), 90000000)

    def single(self):
        self.assertEqual(max_integer([10001]), 10001)

    def begin(self):
        self.assertEqual(max_integer([120920, 3, 4, 5, 67, 7676,
            232, 233]), 120920)

    def errorsStr(self):
        with self.assertRaises(TypeError):
            max_integer([0, '47', 343, 5, 454])

    def errNum(self):
        with self.assertRaises(TypeError):
            max_integer(999)

    def errLists(self):
        with self.assertRaises(TypeError):
            max_integer([44545, 65656, [545, 6565, 6565], 5454])

    def errTuple(self):
        with self.assertRaises(TypeError):
            max_integer([34545, 6666, (99, 7676, 656), 44343, 4322])

    def errDict(self):
        with self.assertRaises(TypeError):
            max_integer([303903, 394034, 2299, 3029, {'err': 545,
                'err2': 3434, 'err3': 343422}, 45453])

    def diffErr(self):
        with self.assertRaises(TypeError):
            max_integer(['rer', {'error': 34343}, (3434, 56656),
                ['34434', 554, 'frfr'], 'errs', 0])

    def diffErr2(self):
        with self.assertRaises(TypeError):
            max_integer({'err': 3443, 'err2': 444545, '47': 47})

    def diffErr3(self):
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3, 4, 5)

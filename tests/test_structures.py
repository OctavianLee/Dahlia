# -*- coding: utf-8 -*-
import unittest

from copy import copy

from structures.arrays import *

class StructureTestCase(unittest.TestCase):
    """Creates a basic testcase to test different data structures.
    """

    def setUp(self):
        """Does nothing
        """
        pass


class ArrayTest(StructureTestCase):

    def setUp(self):
        self.array = Array(25)

    def test_data(self):
        with self.assertRaises(IndexError):
            self.array[100]
        for i in range(25):
            self.array[i] = i
            self.assertEqual(self.array[i], i,
                             "The data are not matched")

    def test_length(self):
        self.assertEqual(self.array.length, 25,
                         "The length is not 25")
        self.assertEqual(len(self.array), 25,
                         "The length is not 25")

    def test_copy(self):
        self.array_copy = copy(self.array)
        for a_value, c_value in zip(self.array, self.array_copy):
            self.assertEqual(a_value, c_value,
                             "Copy failed")

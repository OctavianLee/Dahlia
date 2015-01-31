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
    """Tests the class of Array.
    """

    def setUp(self):
        """Sets up the array.
        """
        self.array = Array(25)

    def test_data(self):
        """Tests whether it can get the data of the array.
        """
        with self.assertRaises(IndexError):
            self.array[100]
        for i in range(25):
            self.array[i] = i
            self.assertEqual(self.array[i], i,
                             "The data are not matched")

    def test_length(self):
        """Tests whether it can get the length of the array.
        """
        self.assertEqual(self.array.length, 25,
                         "The length is not 25")
        self.assertEqual(len(self.array), 25,
                         "The length is not 25")

    def test_copy(self):
        """Tests whether it can copy the array.
        """
        self.array_copy = copy(self.array)
        for a_value, c_value in zip(self.array, self.array_copy):
            self.assertEqual(a_value, c_value,
                             "Copy failed")


class MultiDimensionalArrayTest(StructureTestCase):
    """Tests the class of MultiDimensionalArray.
    """

    def setUp(self):
        """Sets up the array.
        """
        self.array = MultiDimensionalArray(2,2,2)

    def test_data(self):
        """Tests whether it can get the data of the array.
        """
        with self.assertRaises(IndexError):
            self.array[4, 4, 4]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    self.array[i, j, k] = (i, j, k)
                    self.assertEqual(self.array[i, j, k], (i, j, k),
                                     "The data are not matched")

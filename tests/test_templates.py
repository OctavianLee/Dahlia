# -*- coding: utf-8 -*-
import unittest
import random

from dahlia.sorts.templates import SortTemplate


class TestSortTemplate(unittest.TestCase):
    """Tests the SortTemplate class.
    Tests the methods of the SortTemplate class.
    """

    def setUp(self):
        """Sets up some basic testing data.
        """
        collection = range(10)
        self.sorted = SortTemplate(collection)
        collection2 = range(10)
        random.shuffle(collection2)
        self.unsorted = SortTemplate(collection2)

    def test_is_sorted(self):
        """Tests the is_sorted method.
        """
        self.assertEqual(self.sorted.is_sorted(), True)
        self.assertEqual(self.unsorted.is_sorted(), False)

    def test_sort(self):
        """Tests the sort method.
        """
        with self.assertRaises(NotImplementedError):
            self.sorted.sort()

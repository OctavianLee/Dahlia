# -*- coding: utf-8 -*-
import unittest
import random

from dahlia.sorts.bubble_sort import BubbleSort
from dahlia.sorts.insertion_sort import InsertionSort
from dahlia.sorts.selection_sort import SelectionSort
from dahlia.sorts.merge_sort import MergeSort
from dahlia.sorts.pigeonhole_sort import PigeonholeSort


class SortTestCase(unittest.TestCase):
    """Creates a basic testcase to test different sorts.
    """

    def setUp(self):
        """Sets up some basic testing data.
        """
        self.collection = range(25)
        random.shuffle(self.collection)


class BubbleSortTest(SortTestCase):
    """Tests bubble sort.
    """

    def test_sort(self):
        """Tests the sort method.
        Checks the sort method and whether the collection is sorted.
        """
        self.collection = BubbleSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

    def test_quick_sort(self):
        """Tests the quick sort method.
        Checks the quick sort method and whether the collection is sorted.
        """
        self.collection = BubbleSort(self.collection)
        self.collection.quick_sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

    def test_quickest_sort(self):
        """Tests the quickest sort method.
        Checks the quickest sort method and whether the collection is sorted.
        """
        self.collection = BubbleSort(self.collection)
        self.collection.quickest_sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)


class InsertionSortTest(SortTestCase):
    """Tests the insertion sort.
    """

    def test_sort(self):
        """Tests the sort method.
        Checks the sort method and whether the collection is sorted.
        """
        self.collection = InsertionSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

    def test_shell_sort(self):
        """Tests the shell sort method.
        Checks the shell sort method and whether the collection is sorted.
        """
        self.collection = InsertionSort(self.collection)
        self.collection.shell_sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)


class SelectionSortTest(SortTestCase):
    """Tests the selection sort.
    """

    def test_sort(self):
        """Tests the sort method.
        Checks the sort method and whether the collection is sorted.
        """
        self.collection = SelectionSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

    def test_quick_sort(self):
        """Tests the quick sort method.
        Checks the quick sort method and whether the collection is sorted.
        """
        self.collection = SelectionSort(self.collection)
        self.collection.quick_sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)


class MergeSortTest(SortTestCase):
    """Tests the merge sort.
    """

    def test_sort(self):
        """Tests the merge sort method.
        Checks the merge sort method and whether the collection is sorted.
        """
        self.collection = MergeSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)


class PigeonholeSortTest(SortTestCase):
    """Tests the pigeonhole sort.
    """

    def test_sort(self):
        """Tests the pigeonhole sort method.
        Checks the pigeonhole sort method and whether the collection is sorted.
        """
        self.collection = PigeonholeSort(self.collection)
        self.collection.sort()
        self.assertEqual(self.collection.items, range(25))
        self.assertEqual(self.collection.is_sorted(), True)

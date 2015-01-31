# -*- coding: utf-8 -*-
import unittest

from copy import copy

from structures.arrays import *
from structures.lists import *


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
                    
class NodeTest(StructureTestCase):
    """Tests the class of Node.
    """

    def setUp(self):
        """Sets up the Node.
        """
        self.node1 = Node(1, None)
        self.node0 = Node(0, self.node1)

    def test_datum(self):
        """Tests to get the datum of a node.
        """
        self.assertEqual(self.node0.datum, 0,
                         "Cannot get the datum in node2")
        self.assertEqual(self.node1.datum, 1,
                         "Cannot get the datum in node1")

    def test_next(self):
        """Tests to get the next of a node.
        """
        self.assertEqual(self.node0.next, self.node1,
                         "cannot get the next in node2")
        self.node0.next = None
        self.assertEqual(self.node0.next, None,
                         "cannot set the next in node2")
        self.assertEqual(self.node1.next, None,
                         "Cannot get the next in node1")


class LinkedListTest(StructureTestCase):
    """Tests the class of LinkedList.
    """

    def setUp(self):
        """Sets up the list.
        """
        self.linkedlist = LinkedList()
        self.linkedlist.append(1)

    def test_head(self):
        """Tests to get the head of the linked list.
        """
        self.assertEqual(self.linkedlist.head.datum, 1,
                         "Cannot get the head")

    def test_tail(self):
        """Tests to get the tail of the linked list.
        """
        self.assertEqual(self.linkedlist.tail.datum, 1,
                         "Cannot get the head")

    def test_append(self):
        """Tests to append a datum.
        """
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.tail.datum, 2,
                         "Cannot append a datum")

    def test_remove(self):
        """Tests to remove a datum.
        """
        with self.assertRaises(KeyError):
            self.linkedlist.remove(11)
        self.linkedlist.remove(1)
        self.assertEqual(self.linkedlist.tail, self.linkedlist.head,
                         "Cannot remove a datum")

    def test_purge(self):
        """Tests to purge a linked list.
        """
        self.assertEqual(self.linkedlist.is_empty(), False,
                         "Cannot get False when calling is_empty")
        self.linkedlist.purge()
        self.assertEqual(self.linkedlist.is_empty(), True,
                         "Cannot get Treu when calling is_empty")



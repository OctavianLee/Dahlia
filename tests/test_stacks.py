# -*- coding: utf-8 -*-
import unittest
from nose.tools import raises

from structures.stacks import *


class StackTestCase(unittest.TestCase):
    """Creates a basic testcase to test different data structures.
    """

    def setUp(self):
        """Does nothing
        """
        pass

class StackTest(StackTestCase):
    """Creates a class to test the abstract class.
    """

    def setUp(self):
        """Creates a subclass to test.
        """
        class Test(Stack):

              def top(self):
                  super(Test, self).top()

              def purge(self):
                  super(Test, self).purge()

              def push(self, obj):
                  super(Test, self).push(obj)

              def pop(self):
                  super(Test, self).pop()
         
        self.stack = Test()

    @raises(NotImplementedError)
    def test_top(self):
        """Tests the top method.
        """
        self.stack.top()

    @raises(NotImplementedError)
    def test_pop(self):
        """Tests the pop method.
        """
        self.stack.pop()

    @raises(NotImplementedError)
    def test_purge(self):
        """Tests the purge method.
        """
        self.stack.purge()

    @raises(NotImplementedError)
    def test_push(self):
        """Tests the push method.
        """
        self.stack.push(1)


class ArrayStackTest(StackTestCase):
    """Creates a class to test the ArrayStack class.
    """

    def setUp(self):
        """Initializes the stack which will be tests.
        """
        self.stack = ArrayStack(2)

    def test_push(self):
        """Tests the push method.
        """
        self.stack.push(1)
        self.assertEqual(self.stack._count, 1)
        with self.assertRaises(IndexError):
            self.stack.push(1)
            self.stack.push(1)

    def test_top(self):
        """Tests the top method.
        """
        with self.assertRaises(IndexError):
            self.stack.top()
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)

    def test_pop(self):
        """Tests the pop method.
        """
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_purge(self):
        """Tests the purge method.
        """
        self.stack.push(1)
        self.stack.purge()
        with self.assertRaises(IndexError):
            self.assertEqual(self.stack.top(), None)
        self.assertEqual(self.stack._count, 0)


class ListStackTest(StackTestCase):
    """Creates a class to test the ListStack class.
    """

    def setUp(self):
        """Initializes the stack which will be tests.
        """
        self.stack = ListStack()

    def test_push(self):
        """Tests the push method.
        """
        self.stack.push(1)
        self.assertEqual(self.stack._count, 1)

    def test_top(self):
        """Tests the top method.
        """
        with self.assertRaises(IndexError):
            self.stack.top()
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)

    def test_pop(self):
        """Tests the pop method.
        """
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)

    def test_purge(self):
        """Tests the purge method.
        """
        self.stack.push(1)
        self.stack.purge()
        with self.assertRaises(IndexError):
            self.assertEqual(self.stack.top(), None)
        self.assertEqual(self.stack._count, 0)

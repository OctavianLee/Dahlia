# -*- coding: utf-8 -*-
import unittest
from nose.tools import raises

from structures.queues import *


class QueueTestCase(unittest.TestCase):
    """Creates a basic testcase to test different data structures.
    """

    def setUp(self):
        """Does nothing
        """
        pass

class QueueTest(QueueTestCase):
    """Creates a class to test the abstract class.
    """

    def setUp(self):
        """Creates a subclass to test.
        """
        class Test(Queue):

              def head(self):
                  super(Test, self).head()

              def purge(self):
                  super(Test, self).purge()

              def enqueue(self, obj):
                  super(Test, self).enqueue(obj)

              def dequeue(self):
                  super(Test, self).dequeue()
         
        self.queue = Test()

    @raises(NotImplementedError)
    def test_head(self):
        """Tests the head method.
        """
        self.queue.head()

    @raises(NotImplementedError)
    def test_dequeue(self):
        """Tests the dequeue method.
        """
        self.queue.dequeue()

    @raises(NotImplementedError)
    def test_purge(self):
        """Tests the purge method.
        """
        self.queue.purge()

    @raises(NotImplementedError)
    def test_enqueue(self):
        """Tests the enqueue method.
        """
        self.queue.enqueue(1)


class ArrayQueueTest(QueueTestCase):
    """Creates a class to test the ArrayQueue class.
    """

    def setUp(self):
        """Initializes the queue which will be tests.
        """
        self.queue = ArrayQueue(2)

    def test_enqueue(self):
        """Tests the enqueue method.
        """
        self.queue.enqueue(1)
        self.assertEqual(self.queue._count, 1)
        with self.assertRaises(IndexError):
            self.queue.enqueue(1)
            self.queue.enqueue(1)

    def test_head(self):
        """Tests the head method.
        """
        with self.assertRaises(IndexError):
            self.queue.head()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.head(), 1)

    def test_dequeue(self):
        """Tests the dequeue method.
        """
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_purge(self):
        """Tests the purge method.
        """
        self.queue.enqueue(1)
        self.queue.purge()
        with self.assertRaises(IndexError):
            self.assertEqual(self.queue.head(), None)
        self.assertEqual(self.queue._count, 0)


class ListQueueTest(QueueTestCase):
    """Creates a class to test the ListQueue class.
    """

    def setUp(self):
        """Initializes the queue which will be tests.
        """
        self.queue = ListQueue()

    def test_enqueue(self):
        """Tests the enqueue method.
        """
        self.queue.enqueue(1)
        self.assertEqual(self.queue._count, 1)

    def test_head(self):
        """Tests the head method.
        """
        with self.assertRaises(IndexError):
            self.queue.head()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.head(), 1)

    def test_dequeue(self):
        """Tests the dequeue method.
        """
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_purge(self):
        """Tests the purge method.
        """
        self.queue.enqueue(1)
        self.queue.purge()
        with self.assertRaises(IndexError):
            self.assertEqual(self.queue.head(), None)
        self.assertEqual(self.queue._count, 0)

# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from arrays import Array
from lists import LinkedList


class Queue(object):
    """Create a template of the queque.
    
    Attributes:
        count: the length of the current stack.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """Initializes the class.
        """
        self._count = 0

    @abstractmethod
    def head(self):
        """Defines the method of getting the head element.
        """
        raise NotImplementedError

    @abstractmethod
    def enqueue(self, obj):
        """Defines the method of enqueuing.
        """
        raise NotImplementedError

    @abstractmethod
    def purge(self):
        """Defines the method of purging.
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        """Defines the method of dequeuing.
        """
        raise NotImplementedError


class ArrayQueue(Queue):
    """Creates a class of queue using the array.

    Attributes:
        array: the array of the data.
    """

    def __init__(self, length):
        """Initializes the class.
        """
        super(ArrayQueue, self).__init__()
        self._array = Array(length)
        self._head = 0
        self._tail = length - 1

    def purge(self):
        """Cleans the queue.
        """
        while self._count:
            self._array[self._head] = None
            self._head += 1
            if self._head == len(self._array):
                self._head = 0
            self._count -= 1

    def head(self):
        """Gets the head element.
        """
        if self._count == 0: raise IndexError
        return self._array[self._head]

    def enqueue(self, obj):
        """Enqueue.
        """
        if self._count == len(self._array):
            raise IndexError
        self._tail += 1
        if self._tail == len(self._array):
            self._tail = 0
        self._array[self._tail] = obj
        self._count += 1

    def dequeue(self):
        """Dequeue.
        """
        result = self.head()
        self._array[self._head] = None
        self._head += 1
        if self._head == len(self._array):
           self._head = 0
        self._count -= 1
        return result


class ListQueue(Queue):
    """Creates a class of queue using the list.

    Attributes:
        list: the list of the data.
    """

    def __init__(self):
        """Initializes the class.
        """
        super(ListQueue, self).__init__()
        self._list = LinkedList()

    def purge(self):
        """Cleans the queue.
        """
        self._list.purge()
        self._count = 0

    def head(self):
        """Gets the head element.
        """
        if self._count == 0: raise IndexError
        return self._list.head.datum

    def enqueue(self, obj):
        """Enqueue.
        """
        self._list.append(obj)
        self._count += 1

    def dequeue(self):
        """Dequeue.
        """
        result = self.head()
        self._list.remove(result)
        self._count -= 1
        return result


class Deque(Queue):
    """Create a template of the deque inherited from the Queue class.
    """

    def __init__(self):
        """Initializes the class.
        """
        super(Deque, self).__init__()

    @abstractmethod
    def tail(self):
        """Defines the method of getting the tail element.
        """
        raise NotImplementedError

    @abstractmethod
    def enqueue_head(self, obj):
        """Defines the method of enqueuing the head element.
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue_tail(self):
        """Defines the method of dequeuing the tail element.
        """
        raise NotImplementedError

    def enqueue_tail(self, obj):
        """Defines the method of enqueuing the tail element.
        It is implemented by the enqueue method.
        """
        self.enqueue(obj)

    def dequeue_head(self):
        """Defines the method of dequeuing the head element.
        It is implemented by the dequeue method.
        """
        return self.dequeue()


class ArrayDeque(ArrayQueue, Deque):
    """Creates a class of deque using the array inherited from ArrayQueue and Deque.
    """

    def __init__(self, length):
        """Initializes the class.
        """
        super(ArrayDeque, self).__init__(length)

    def tail(self):
        """Gets the tail element.
        """
        if self._count == 0: raise IndexError
        return self._array[self._tail]

    def enqueue_head(self, obj):
        """Enqueues an object from the head.
        """
        if self._count == len(self._array):
            raise IndexError
        self._head = (self._head-1) if self._head else (len(self._array)-1)
        self._array[self._head] = obj
        self._count += 1

    def dequeue_tail(self):
        """Dequeues from the tail.
        """
        result = self.tail()
        self._array[self._tail] = None
        self._tail = (self._tail-1) if self._tail else (len(self._array)-1)
        self._count -= 1
        return result


class ListDeque(ListQueue, Deque):
    """Creates a class of deque using the list inherited from ListQueue and Deque.
    """

    def __init__(self):
        """Initializes the class.
        """
        super(ListDeque, self).__init__()

    def tail(self):
        """Gets the tail element.
        """
        if self._count == 0: raise IndexError
        return self._list.tail.datum

    def enqueue_head(self, obj):
        """Enqueues an object from the head.
        """
        self._list.prepend(obj)
        self._count += 1

    def dequeue_tail(self):
        """Dequeues from the tail.
        """
        result = self.tail()
        self._list.remove(result)
        self._count -= 1
        return result

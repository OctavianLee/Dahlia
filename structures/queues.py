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
        self.__array = Array(length)
        self.__head = 0
        self.__tail = length - 1

    def purge(self):
        """Cleans the queue.
        """
        while self._count:
            self.__array[self.__head] = None
            self.__head += 1
            if self.__head == len(self.__array):
                self.__head = 0
            self._count -= 1

    def head(self):
        """Gets the head element.
        """
        if self._count == 0: raise IndexError
        return self.__array[self.__head]

    def enqueue(self, obj):
        """Enqueue.
        """
        if self._count == len(self.__array):
            raise IndexError
        self.__tail += 1
        if self.__tail == len(self.__array):
            self.__tail = 0
        self.__array[self.__tail] = obj
        self._count += 1

    def dequeue(self):
        """Dequeue.
        """
        result = self.head()
        self.__array[self.__head] = None
        self.__head += 1
        if self.__head == len(self.__array):
           self.__head = 0
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
        self.__list = LinkedList()

    def purge(self):
        """Cleans the queue.
        """
        self.__list.purge()
        self._count = 0

    def head(self):
        """Gets the head element.
        """
        if self._count == 0: raise IndexError
        return self.__list.head.datum

    def enqueue(self, obj):
        """Enqueue.
        """
        self.__list.append(obj)
        self._count += 1

    def dequeue(self):
        """Dequeue.
        """
        if self._count == 0: raise IndexError
        result = self.head()
        self.__list.remove(result)
        self._count -= 1
        return result

# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from arrays import Array
from lists import LinkedList


class Stack(object):
    """Create a template of the stack.
    
    Attributes:
        count: the length of the current stack.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        """Initializes the class.
        """
        self._count = 0

    @abstractmethod
    def top(self):
        """Defines the method of getting the top element.
        """
        raise NotImplementedError

    @abstractmethod
    def push(self, obj):
        """Defines the method of pushing.
        """
        raise NotImplementedError

    @abstractmethod
    def purge(self):
        """Defines the method of purging.
        """
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        """Defines the method of popping.
        """
        raise NotImplementedError


class ArrayStack(Stack):
    """Creates a class of stack using the array.

    Attributes:
        array: the array of the data.
    """

    def __init__(self, length):
        """Initializes the class.
        """
        super(ArrayStack, self).__init__()
        self.__array = Array(length)
    
    def purge(self):
        """Cleans the stack.
        """
        while self._count:
            self.__array[self._count-1] = None
            self._count -= 1

    def push(self, obj):
        """Pushes an object into the stack.
        """
        if self.__array == len(self.__array):
            raise IndexError
        self.__array[self._count] = obj
        self._count += 1

    def pop(self):
        """Pop an object up the stack.
        """
        if self._count == 0: raise IndexError
        self._count -= 1
        result = self.__array[self._count]
        return result

    def top(self):
        """Get the top object of a stack.
        """
        if self._count == 0: raise IndexError
        return self.__array[self._count-1]


class ListStack(Stack):
    """Creates a class of stack using the linked list.

    Attributes:
        list: the linked list of the data.
    """

    def __init__(self):
        """Initializes the class.
        """
        super(ListStack, self).__init__()
        self.__list = LinkedList()

    def purge(self):
        """Cleans the stack.
        """
        self.__list.purge()
        self._count = 0

    def push(self, obj):
        """Pushes an object into the stack.
        """
        self.__list.append(obj)
        self._count += 1

    def pop(self):
        """Pop an object up the stack.
        """
        if self._count == 0: raise IndexError
        result = self.__list.head.datum
        self.__list.remove(result)
        self._count -= 1
        return result

    def top(self):
        """Get the top object of a stack.
        """
        if self._count == 0: raise IndexError
        return self.__list.head.datum

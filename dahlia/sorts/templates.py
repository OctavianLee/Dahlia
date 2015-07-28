# -*- coding: utf-8 -*-
from __future__ import print_function


class SortTemplate(object):

    """ Creates a template class for sorting.
    When someone need to implement a sorting method, 
    he should create a class and inherite this to help build the structure.

    Attributes:
        items: mutable collection, the elements we need to sort.
        length: integer, the length of items.
    """

    def __init__(self, collection):
        """Inits the class.

        Args:
            collection: a mutable collection.
        """
        self.__items = collection
        self.__length = len(self.items)

    @property
    def length(self):
        """Gets the property of the length.
        """
        return self.__length

    @property
    def items(self):
        """Gets the property of the items.
        """
        return self.__items

    @items.setter
    def items(self, values):
        """Sets the property of the items.
        """
        self.__items = values

    def exchange(self, pos1, pos2):
        """Exchanges the elements between two positions in items.

        Helps to record the step of exchanging.

        Args:
            pos1: one element's position in items.
            pos2: another element's position in items.
        """
        self.items[pos1], self.items[pos2] = self.items[pos2], self.items[pos1]

    def is_sorted(self):
        """Check whether the items is sorted.

        Returns:
            True: the items is sorted.
            False: the items is not sorted.
        """
        for i in range(self.length - 1):
            if self.items[i] > self.items[i + 1]: return False
        return True

    def show(self):
        """Shows all items.

        """
        for item in self.items:
          print(item)

    def sort(self):
        """Creates the sort method here.

        Rasies:
            NotImplemented
        """
        raise NotImplementedError

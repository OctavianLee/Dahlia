# -*- coding: utf-8 -*-
from .templates import SortTemplate


class InsertionSort(SortTemplate):
    """Creates a class to implement the insertion sort
    """

    def sort(self):
        """uses the insertion sort algorithm to sort.
        This is a basic insertion sort algorithm
        """

        for j in range(1, self.length):
            i = j - 1
            index = self.items[j]
            while index < self.items[i] and i >=0:
                self.items[i + 1] = self.items[i]
                i -= 1
            self.items[i + 1] = index

# -*- coding: utf-8 -*-
from .templates import SortTemplate


class RadixSort(SortTemplate):
    """Creates a class to implement the radix sort.
    """

    def sort(self):
        """Uses the radix sort algorithm to sort.
        This is a radix sort algorithm.
        """
        bucket = [[] for i in range(self.length+1)]

    def __maxbit(self):
        maxbit = 1
        base = 10
        for item in self.items:
            while item >= base:
                base *= 10
                maxbit += 1
        return maxbit

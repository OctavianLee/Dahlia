# -*- coding: utf-8 -*-
from .templates import SortTemplate


class SelectionSort(SortTemplate):
    """Creates a class to implement the selection sort.
    """

    def sort(self):
        """Uses the section sort algorithm to sort.
        This is a basic section sort algorithm.
        """

        for i in range(self.length):
            min = i
            for j in range(i+1, self.length):
                if self.items[min] > self.items[j]:
                    min = j
            self.exchange(i, min)

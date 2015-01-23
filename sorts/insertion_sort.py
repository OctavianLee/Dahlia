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

    def shell_sort(self):
        """uses the shell sort algorithm to sort.
        This is a shell sort algorithm
        """

        gap = self.length // 3 + 1
        while gap >= 1:
            for j in range(gap, self.length):
                i = j - gap
                index = self.items[j]
                while index < self.items[i] and i>=0:
                    self.items[i + gap] = self.items[i]
                    i = i - gap
                self.items[i + gap] = index
            gap = gap // 3

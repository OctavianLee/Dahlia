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
    
    def quick_sort(self):
        """Uses the quick sort algorithm to sort.
        This is a quick section sort algorithm.
        """
        self.__quick_sort_helper(0, self.length-1)

    def __quick_sort_helper(self, first, last):
        """Does quick sort recursively.
        """
        if first < last:
            j = self.__partition(first, last)
            self.__quick_sort_helper(first, j-1)
            self.__quick_sort_helper(j+1, last)

    def __partition(self, first, last):
        """Sorts one partition's element.
        """

        pivot = self.items[first]
        left = first + 1
        right = last
        while True:
            while left <= right and self.items[left] <= pivot: left += 1
            while self.items[right] >= pivot and left <= right: right -= 1
            if left > right: break
            self.exchange(left, right)
        self.exchange(first, right)
        return right

# -*- coding: utf-8 -*-
from .templates import SortTemplate


class MergeSort(SortTemplate):
    """Creates a class to implement the merge sort.
    """

    def sort(self):
        """Uses the merge sort algorithm to sort.
        This is a merge sort algorithm.
        """
        self.items = self.__merge_sort(self.items)

    def __merge_sort(self, items):
        length = len(items)
        if length <= 1: return items
        middle = length // 2
        left = self.__merge_sort(items[:middle])
        right = self.__merge_sort(items[middle:])
        return self.__merge(left, right)

    def __merge(self, left, right):
        result = []
        i, j = 0, 0
        left_length, right_length = len(left), len(right)
        while i < left_length and j < right_length:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        if left[i:]: result += left[i:]
        if right[j:]: result += right[j:]
        return result

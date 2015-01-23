# -*- coding: utf-8 -*-
from .templates import SortTemplate


class BubbleSort(SortTemplate):
    """Creates a class to implement the bubble sort
    """

    def sort(self):
        """uses the bubble sort algorithm to sort.
        This is a basic bubble sort algorithm
        """
        times = self.length - 1 # saves costs
        for i in range(self.length):
            for j in range(times - i):
                if self.items[j] > self.items[j+1]:
                    self.exchange(j, j+1)

    def quick_sort(self):
        """uses the bubble sort algorithm to sort a little bit faster.
        Uses a 'index' to mark the last exchange
        """
        index = self.length - 1# it starts at the last element
        temp = 0
        while index > 0:
            for i in range(index):
                temp = i
                if self.items[i] > self.items[i+1]:
                    self.exchange(i, i+1)
                    temp = i
            index = temp

    def quickest_sort(self):
        """uses the fastest bubble sort algorithm to sort.
        In one turn,
        sorts from the beginning to the end and from the end to the beginning.
        Uses a 'up' to mark the last exchange from the beginbing to the end.
        Uses a 'down' to mark the lasst echange from the end to the beginning.
        """
        up = self.length - 1# it starts at the last element
        down = 0
        temp = up
        while up > down:
            for i in range(down, up):
                if self.items[i] > self.items[i+1]:
                    self.exchange(i, i+1)
                    temp = i
            up = temp
            for i in range(up, down, -1):
                if self.items[i] < self.items[i-1]:
                    self.exchange(i, i-1)
                    temp = i
            down = temp

# -*- coding: utf-8 -*-
from .templates import SortTemplate


class PigeonholeSort(SortTemplate):
    """Creates a class to implement the pigeonhole sort.
    """

    def sort(self):
        """Uses the pigeonhole sort algorithm to sort.
        This is a pigeonhole sort algorithm.
        """
        pigeon_hole = [[] for i in range(self.length+1)]
        """
        #The comment code is a special one of this algorithm.
        for item in self.items:
            pigeon_hole[item] += 1
        
        index = 0
        for i in range(self.length+1):
            for k in range(pigeon_hole[i]):
                self.items[index] = i
                index += 1
        """

        for item in self.items:
            pigeon_hole[item] += [item]

        index = 0
        for hole in pigeon_hole:
            if hole != []:
                for item in hole:
                    self.items[index] = item
                    index += 1

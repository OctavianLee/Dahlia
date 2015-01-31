# -*- coding: utf-8 -*-


class Array(object):
    """This is a implement of the one-dimensional array.

    Temporarily, the class use the List to implement a basic array.
    In the future, it will carry it out with the dictionary for efficiency.

    Attributes:
        length: integer, the length of the array.
        data: mutable collection, the data of the array.
    """

    def __init__(self, length):
        """Initializes the class.

        Args:
            length: the lenght of the array.
        """
        #the length must be larger than 0
        assert length > 0
        self.__length = length
        self.__data = [None for i in range(length)]

    def __len__(self):
        """Get the length of the array.

        Sometimes, it is nessary to use the built-in function to get the length
        of the array, however len(self._data) is inefficient.
        Just returning the value of lenght will be a good choice.
        """
        return self.__length

    @property
    def length(self):
        """Gets the value of the length.
        """
        return self.__length

    def __copy__(self):
        """Implements the method of copying the array.
        This is a shallow copy.
        """
        result = Array(self.__length)
        for i, datum in enumerate(self.__data):
            result.__data[i] = datum
        return result

    def __get_offset(self, offset):
        """Gets the offset of the array.
        """
        #checks the overflow of the offset.
        if offset < 0 or offset >= self.__length:
            raise IndexError
        return offset

    def __getitem__(self, index):
        """Overloads the __getitem__ method.
        """
        return self.__data[self.__get_offset(index)]

    def __setitem__(self, index, value):
        """Overloads the __setitem__ method.
        """
        self.__data[self.__get_offset(index)] = value


class MultiDimensionalArray(object):
    """This is a implement of the mutil-dimensional array.

    Attributes:
        length: integer, the length of the array.
        data: mutable collection, the data of the array.
        dimensions: tuple, the length of different dimensions.
        factor: mutable collection, records the index of array 
                which reach different bounds.

                For a[2][2], the factor is [2,1].When reaching the a[1][1]
                it is equal to array[1 * 2 + 1].
    """

    def __init__(self, *dimensions):
        """Initializes the class.

        Args:
            dimensions: tuple, the length of different dimensions.
        """
        self.__length = len(dimensions)
        self.__dimensions = dimensions
        self.__factors = Array(self.__length)
        product = 1
        index = self.__length - 1
        for i in range(index, -1, -1):
            self.__factors[i] = product
            product *= self.__dimensions[i]
        self.__data = Array(product)

    def __get_offset(self, indices):
        """Gets the offeset of the array.
        """
        if len(indices) != self.__length:
            raise IndexError
        offset = 0
        for i, dim in enumerate(self.__dimensions):
            if indices[i] < 0 or indices[i] >= dim: raise IndexError
            offset += self.__factors[i] * indices[i]
        return offset

    def __getitem__(self, indices):
        """Overloads the __getitem__ method.
        """
        return self.__data[self.__get_offset(indices)]

    def __setitem__(self, indices, value):
        """Overloads the __setitem__ method.
        """
        self.__data[self.__get_offset(indices)] = value


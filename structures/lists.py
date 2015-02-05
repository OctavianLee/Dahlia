# -*- coding: utf-8 -*-

class Node(object):
    """Creates a class of node.
    For different lists, 
    a node is a basic element to record data and the next node.

    Attributes:
        datum: a datum of a node.
        next: the next of a node.
    """
    def __init__(self, datum, next):
        """Initializes the class.
        
        Args:
            datum: the datum of a node.
            next: the next of a node.
        """
        self.__datum = datum
        self.__next = next

    @property
    def datum(self):
        """Gets a datum.
        """
        return self.__datum
        
    @property
    def next(self):
        """Gets the next.
        """
        return self.__next

    @next.setter
    def next(self, next):
        """Sets the next node
        """
        self.__next = next


class LinkedList(object):
    """Creates a class of the linked list.
    This a simplest linked list becaues of implementing some basic methods.
    
    Such as:
        Appends and removes a node.
        Purges and Tests if it is empty.

    Attributes:
        head: the head of a linked list.
        tail: the tail of a linked list.
    """

    def __init__(self):
        """Initializes the class.
        """
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        """Gets the head.
        """
        return self.__head

    @property
    def tail(self):
        """Gets the tail.
        """
        return self.__tail

    def purge(self):
        """Cleans the linked list
        """
        self.__head = None
        self.__tail = None

    def is_empty(self):
        """Test whether the linked list is empty.
        """
        return self.__head is None

    def append(self, item):
        """Adds a node.
        
        Args:
            item : the item it will add.
        """
        #Generates the node.
        datum = Node(item, None)
        #For the first node in a linked list, it will change the head.
        if self.__head is None:
            self.__head = datum
        else:
            self.__tail.next = datum
        self.__tail = datum

    def prepend(self, item):
        """Preadds a node.
        
        Args:
            item : the item it will preadd.
        """
        #Generates the node.
        datum = Node(item, self.__head)
        if self.__head is None:
            self.__tail = datum
        self.__head = datum

    def remove(self, item):
        """removes a node.
        
        Args:
            item : the item it will remove.
        """
        pointer = self.__head
        prepointer = None
        #Finds the item
        while pointer and pointer.datum != item:
            prepointer = pointer
            pointer = pointer.next
        #Raise the error when not finding the item.
        if pointer is None: raise KeyError
        #When the linked list has one node, it will sets the head.
        if pointer == self.__head:
            self.__head = pointer.next
        else:
            prepointer.next = pointer.next
        if pointer == self.__tail:
            self.__tail = prepointer

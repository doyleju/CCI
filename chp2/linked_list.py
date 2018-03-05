from random import randint


class ListNode(object):
    """Class to create node instance in singly linked list.

    To use:
        this_node = ListNode(10) list = 10 -> None
        other_node = ListNode(20, this_node) list = 20 -> 10 -> None
        another_node = ListNode(30)
        another_node.set_next(other_node) list = 30 -> 20 -> 10 -> None
        this_node.set_value(5) list = 30 -> 20 -> 5 -> None
    """

    # use __slots__ for improved memory management
    __slots__ = '_value', '_next'

    def __init__(self, value: int, next_node=None):
        """Initialise ListNode class.

        Args:
            value (int): value of ListNode instance will be set to this
            next_node (ListNode): Next node in list. Default None.
        """

        # check the arguments are of correct type
        if isinstance(value, int):
            self._value = value
        else:
            raise ValueError('value must be an integer')

        if isinstance(next_node, ListNode) or next_node is None:
            self._next = next_node
        else:
            raise ValueError('next_node must be a ListNode or None')

    def __str__(self):
        return str(self._value)

    def set_value(self, value):
        """Set the integer value of this node."""
        self._value = value

    def get_value(self):
        """Return the integer value of this node."""
        return self._value

    def set_next(self, next_node):
        """Link this node to the next_node - singly linked list."""
        self._next = next_node

    def get_next(self):
        """Return the next_node that this node is linked to"""
        return self._next


class SinglyLinkedList(object):
    """Class for singly linked list."""

    # use __slots__ for improved memory management
    __slots__ = '_head', '_tail', '_current', '_values', '_size'

    def __init__(self):
        """Initialise SinglyLinkedList.

        Args:
            No arguments.
            
        SinglyLinkedList is initialised empty.
        _head and _tail default None. _size default = 0
        """

        self._head = self._tail = None
        self._size = 0

    # inbuilt to iterate through all values of the list
    def __iter__(self):
        self._current = self._head
        while self._current:
            yield self._current.get_value()
            self._current = self._current.get_next()

    # used to print values of the list
    def __str__(self):
        self._values = [str(x) for x in (self)]
        return '[' + ', '.join(self._values) + ']'

    # O(1) time to return length of the list
    def __len__(self):
        return self._size

    # return the head of the list
    def head(self):
        """Return the _head of this list instance."""
        return self._head

    # return boolean on number of list items - False if no items
    def is_empty(self):
        """Return boolean True if _size is 0 else False"""
        return self._size == 0

    # add a new value to head of the list
    def prepend(self, value):
        """Add a new value (ListNode) to the start of the linked list

        Args:
            value (int): this integer value will be assigned to a new ListNode

        Return:
            _head (ListNode): new head of the list which contains value
        """

        if self._head is None:
            self._head = self._tail = ListNode(value, self._head)
        else:
            self._head = ListNode(value, self._head)
        self._size += 1
        return self._head

    # add a new value to head of the list
    def append(self, value):
        """Add a new value (ListNode) to the end of the linked list

        Args:
            value (int): this integer value will be assigned to a new ListNode

        Return:
            _tail (ListNode): new tail of the list which contains value
        """

        if self._head is None:
            self._head = self._tail = ListNode(value, self._head)
        else:
            self._tail._next = ListNode(value)
            self._tail = self._tail._next

        self._size += 1
        return self._tail

    # used for testing to create random lists
    def random(self, length, min_, max_):
        """Create a singly linked list with random integers.

        Args:
            length (int): create list with this number of ListNodes
            min_ (int): minimum value for random integer values
            max_ (int): maximum value for random integer values

        Used for testing to create linked lists of random sizes and values

        Return:
            self - singly linked list instance with random integers
        """

        self._head = self._tail = None

        for _ in range(length):
            self.prepend(randint(min_, max_))
            self._size += 1

        return self

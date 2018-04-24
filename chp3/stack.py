class Empty(Exception):
    """Class used to raise Exception when stack is empty."""
    pass

class StackNode(object):
    """Class to create node instance in a stack."""

    # use __slots__ for improved memory management
    __slots__ = '_value', '_next'

    def __init__(self, value: int, next_node=None):
        """Initialise StackNode class.
        Args:
            value (int): value of StackNode instance will be set to this.
            next_node (StackNode): Next node in stack. Default None.
        """

        # check the init arguments are of the correct type before assignment
        if isinstance(value, int):
            self._value = value
        else:
            raise ValueError('value must be an integer')

        if isinstance(next_node, StackNode) or next_node is None:
            self._next = next_node
        else:
            raise ValueError('next_node must be a StackNode or None')

    def __str__(self):
        """Inbuilt str method for printing node value."""
        return str(self._value)

    def get_value(self):
        """Return the integer value of this node."""
        return self._value

    def get_next(self):
        """Return the next_node that this node is linked to."""
        return self._next
    
class Stack(object):
    """Class for stack with O(1) time push and pop methods."""
    
    def __init__(self):
        """Initialise stack. No arguments. Top defaults to None."""
        self._top = None
        
    def is_empty(self):
        """Check if stack is empty. Check for presence of top node."""
        return self._top == None
    
    def peek(self):
        """Check value of top node on stack. Raise exception if empty."""
        if self.is_empty():
            raise Empty("The stack is empty - can not peek")
        else:
            return self._top.get_value()
        
    def push(self, value):
        """Add a new value to top of stack."""
        # Create a new top node linked to current top node
        self._top = StackNode(value, self._top)
        return self._top
        
    def pop(self):
        """Remove the top node from stack and returns its value. Raise exception if empty."""
        if self.is_empty():
            raise Empty("The stack is empty - can not pop")    
        else:
            # get the current value at the top of the stack
            _top_value = self._top.get_value()
            
            # move the top value to be the next item on the stack    
            self._top = self._top.get_next()
            return _top_value        
    
class StackMin(Stack):
    """Extends the stack class to allow O(1) time search for the min value in the stack."""
    
    def __init__(self):
        """Initialise Stack. No arguments. Use superclass Stack to hold minimum values."""
        super().__init__()
        self._min_values = Stack()
        
    def push(self, value):
        """Add a new value to top of Stack and optionally add to min values stack.
        Args:
            value (int): create StackNode with this integer value and assign to top.
        Return:
            None
        """
        # The new top node links to the current top node
        self._top = StackNode(value, self._top)
        
        # Check if we are pushing the first value onto stack or not
        if self._min_values.is_empty():
            # This is the first value onto stack so has to be the min
            self._min_values.push(value)
        else:
            # we must keep copies of equivalent min values in this list
            # if not we will get out of sync when popping values off
            if self._min_values.peek() >= value:
                self._min_values.push(value)
            
        
    def pop(self):
        """Remove value from top of Stack and optionally remove from min values stack.
        Args: 
            None
         Returns:
             Value from top node of stack - which has just been removed.
         """
        # Raise an exception if the stack is empty
        if self.is_empty():
            raise Empty("The stack is empty - can not pop")
        else:
            _top_value = self._top.get_value()
            
            # if popping off current min value remove it from our min value stack
            if self._min_values.peek() == _top_value:
                self._min_values.pop()
            
            # set top value to be the next item on the stack    
            self._top = self._top.get_next()
            return _top_value
        
    def get_min(self):
        """Get minimum value from the stack in O(1) time.
        Args: 
            None
         Returns:
             Value from top node of min values stack.
         """
        # Raise an exception if the stack is empty - can't be a min value
        if self.is_empty():
            raise Empty("The min values stack is empty - can not get min value")
        else:
            # if we have elements on our stack - current min is on top of _min_values stack
            return self._min_values.peek()

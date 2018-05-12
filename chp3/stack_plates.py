from stack import *

class StackPlates(object):
    """Class to manage multiple stacks of fixed size."""
    
    def __init__(self, stack_size = 10):
        """Initialise StackPlates class.
        Args:
            stack_size (int): max number of nodes - default 10
        """
        # store our stacks in an array - initialise with an empty stack
        self._stacks = [Stack()]

        # each stack has a max size which is the same for all stacks
        self._max_size = stack_size
        
    def display(self):
        for stack in self._stacks:
            print(stack)

    def peek(self):
        """Check value of top node on current/last stack.
        Raise exception if all stacks are empty.
        Args:
            None 
        Return: self._stacks[-1].peek() (int): Value on top of current stack.
        """
        
        # Last stack should only be empty if all stacks are empty
        # However, also checking length of stacks array to be certain
        if self._stacks[-1].is_empty() and len(self._stacks) <= 1:
            raise Empty("The stacks are empty - can not peek")
        else:
            return self._stacks[-1].peek()
        
    def _pop(self, index=-1):
        """Remove a node/value from a stack in the list.
        Default behaviour is to remove node from the last stack in the list.
        Removes the stack from the list if the last node has been removed.
        Args:
            index (int): remove node from the stack at this index in list.
        Return:
            self._top_value (int): Value which has been removed from the stack at index.
        """
        
        # Ensure the stack is not already empty
        if self._stacks[index].is_empty():
            #raise Empty('The current stack is Empty - can not pop')
            raise Empty('The stack at index {} is Empty - can not pop'.format(index))
        
        # Check if this is the last node/value on the current/last stack
        if self._stacks[index].get_size() == 1:

            # pop the last node value from the current stack
            self._top_value = self._stacks[index].pop()
            
            # remove this empty stack from the list unless it is the last stack
            # we always want to keep an empty stack at index 0 if everything is empty
            # Deleting the stack from the list ensures we don't get gaps in the list
            if len(self._stacks) > 1:
                del self._stacks[index]
            
            return self._top_value

        # more than one node so just pop the top value off this stack
        return self._stacks[index].pop()
        
    def pop(self):
        """Remove a node/value from the current/last stack in the list.
        Removes the stack from the list if the last node has been removed.
        Args:
            None.
        Return:
            self._top_value (int): Value which has been removed from the current/last stack.
        """
        
        # call internal method shared with popAt() to pop value
        return self._pop()
    
    def popAt(self, index):
        """Remove a node/value from specific stack at particular index.
        Removes the stack from the list if the last node has been removed.
        Args:
            index (int): Stack position in the list.
        Return:
            self.stacks[index]._top (int): Value which has been removed from the current stack.
        """
        
        # call internal method shared with pop() to pop value
        return self._pop(index)
    
    def push(self, value):
        """Add a value to the current/last stack.
        Adds the value to the top of the last stack.
        Creates new stack if the last stack is full.
        Args:
            value (int): Create StackNode with this integer value and add to stack.
        Return:
            stacks[-1]._top (int): Value which has been added to the stack.
        """
        
        # check if the current/last stack has capacity for another node/value
        if self._stacks[-1].get_size() >= self._max_size:

            # create a new empty stack as previous was full
            self._stacks.append(Stack())

        # add this value to the top of the current/last stack
        return self._stacks[-1].push(value)

from stack import *

class MyQueue(object):
    """Manage a queue by using two stacks."""
    
    def __init__(self):
        """Initialise MyQueue class. No arguments."""
        # main stack will be used when enqueueing values
        self._main = Stack()
        # reversed stack will be used when dequeing or peeking
        self._reversed = Stack()
        
    def deque(self):
        """Remove a value from the front of the queue.
        Removes value from bottom of the main stack or top of the reversed stack.
        Args:
            None.
        Return:
            self._reversed._top (int): value from the front of queue
        """
        
        # raise an Exception if both stacks are empty - no values
        if self._main.is_empty() and self._reversed.is_empty():
            raise Empty('MyQueue is empty. Can not deque node.')
        
        # if reversed stack is empty - node at front of queue is at bottom of main stack
        elif self._reversed.is_empty():

            while not self._main.is_empty():
                # copy all nodes from main stack to reversed stack
                self._reversed.push(self._main.pop())
                
        # item at front of queue is on top of reversed stack 
        return self._reversed.pop()
    
    def enqueue(self, value):
        """Add a value to the queue.
        Adds the value to the top of the main stack - which is back of the queue.
        Args:
            value (int): Create StackNode with this integer value and add to stack.
        Return:
            self._main._top (int): The value just added to the top of main stack (back of queue)
        """
        
        # values must be on main stack to enqueue new value
        if not self._reversed.is_empty():

            # copy all nodes from reversed stack to main stack
            while not self._reversed.is_empty():
                self._main.push(self._reversed.pop())
                
        # push the new value to back of the queue (top of main stack) 
        return self._main.push(value)
        

from stack import *

def stack_sort(unsorted):
    """Put stack nodes in sorted order
    Args:
        unsorted (Stack): stack of random length with integer nodes out of order 
    Returns:
        sorted (Stack): stack of integer nodes in sorted order with largest on top
    """
    
    # create a second stack to hold the nodes in sorted order
    sorted_stack = Stack()
    # will use a temp value to hold node value when transferring from unsorted to sorted
    temp_value = None
    
    # Keep processing until we have moved all nodes from the unsorted stack to the sorted
    while not unsorted.is_empty():
        
        temp_value = unsorted.pop()
        
        # We want to place the temp value on the sorted stack
        # So move all nodes larger than temp value over to unsorted stack temporarily
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp_value:
            unsorted.push(sorted_stack.pop())
         
        # temp value can now be placed on sorted stack in correct place    
        sorted_stack.push(temp_value)        
        
        # move all nodes which are in order from unsorted to sorted   
        while not unsorted.is_empty() and unsorted.peek() > sorted_stack.peek():
            sorted_stack.push(unsorted.pop())
    
    # unsorted stack is now empty and all nodes are in correct order on sorted stack        
    return sorted_stack

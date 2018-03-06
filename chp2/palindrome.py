"""Module to check if a singly linked list is a palindrome"""

from linked_list import *
from collections import deque


def is_palindrome_stack(head_node):
    """Function to check if singly linked list is a palindrome

    Args:
        head_node (ListNode): linkded list node containing integer value 1-9

    Returns:
        True/False
    """

    if not isinstance(head_node, ListNode) and head_node is not None:
        raise ValueError('head_node must be type ListNode or None')

    # empty node is a palindrome and single node is a palindrome
    if head_node is None or head_node.get_next() is None:
        return True

    # hold the first half of list in stack
    stack = deque()

    # fast runner will make 2 moves for each one of slow runner
    slow = fast = head_node

    # move fast runner to end of list and slow runner to middle
    while fast and fast.get_next():
        stack.append(slow.get_value())
        slow = slow.get_next()
        fast = fast.get_next().get_next()

    # if odd number of elements
    # slow runner is on the exact middle value - fast is on the last value
    # ignore this value as middle of palindrome
    if fast:
        slow = slow.get_next()

    # move slow runner along remainder of list until end
    while slow:
        # pop the next value off the stack
        value = stack.pop()

        # compare slow runner value and stack value
        if value != slow.get_value():
            return False

        # move to next runner value
        slow = slow.get_next()

    # all values have been compared so must be a palindrome
    return True


def reverse_list_copy(head_node):
    """Function to make reverse copy of singly linked list

    Args:
        head_node (ListNode): linkded list head_node containing integer value 1-9

    To Use:
        head_node_r = reverse_list_copy(head_node)

    Returns:
        head_node_r (ListNode): head node of copied, reversed linked list
    """

    current = head_node

    # start a new list
    head_node_r = None

    while current:
        # prepend a new head node to reversed list using current value
        head_node_r = ListNode(current.get_value(), head_node_r)
        current = current.get_next()

    # return the head node of the reversed list
    return head_node_r


def is_palindrome_reverse(head_node):
    """Function to check if singly linked list is a palindrome

    Args:
        head_node (ListNode): linkded list node containing integer value 1-9

    Returns:
        True/False
    """

    # type check head_node
    if not isinstance(head_node, ListNode) and head_node is not None:
        raise ValueError('head_node must be type ListNode or None')

    # empty node is a palindrome and single node is a palindrome
    if head_node is None or head_node.get_next() is None:
        return True

    # get a reversed copy of the list for comparison
    head_node_r = reverse_list_copy(head_node)

    # create a runner for normal and reversed list
    runner = head_node
    runner_r = head_node_r

    # compare all the values of both lists
    while runner and runner_r:
        # if any value is different it is not a palindrome
        if runner.get_value() != runner_r.get_value():
            return False
        runner = runner.get_next()
        runner_r = runner_r.get_next()

    # all values have been compared so must be a palindrome
    return True

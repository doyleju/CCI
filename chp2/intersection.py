"""Module to check if two singly linked lists intersect"""

from linked_list import *


def intersect_node(longer, shorter):
    """Function to find the intersect node of two singly linked lists.

    Args:
        longer (ListNode): linkded list head node of the longer list
        shorter (ListNode): linkded list head node of the shorter list

    Returns:
        intersect (ListNode): node where the lists intersect
    """

    # ignore the start nodes of longer list - make lists same length
    for _ in range(len(longer) - len(shorter)):
        longer = longer.get_next()

    # same length now so compare node by node to find the intersect node
    while longer:
        if longer is shorter:
            return longer

        longer = longer.get_next()
        shorter = shorter.get_next()

    # should never reach here - tails matched previously
    return None


def compare_lengths(head_node1, head_node2):
    """Function to compare the lengths of two singly linked lists.

    Args:
        head_node1 (ListNode): linkded list node containing integer value 1-9
        head_node2 (ListNode): linkded list node containing integer value 1-9

    Returns:
        longer (ListNode): reference to longer list head node
        shorter (ListNode): reference to shorter list head node
    """

    # get length of both lists
    length1 = len(head_node1)
    length2 = len(head_node2)

    # assign names
    if length1 > length2:
        longer, shorter = head_node1, head_node2
    else:
        longer, shorter = head_node2, head_node1

    # return head_nodes
    return longer, shorter


def tails_same(head_node1, head_node2):
    """Function to compare the tail nodes of two singly linked lists.

    Args:
        head_node1 (ListNode): linkded list node containing integer value 1-9
        head_node2 (ListNode): linkded list node containing integer value 1-9

    Returns:
        True/False: True if tail1 and tail2 are the same node else False
    """

    current1, current2 = head_node1, head_node2

    # get the tail of list1
    while current1.get_next() is not None:
        current1 = current1.get_next()

    tail1 = current1

    # get the tail of list2
    while current2.get_next() is not None:
        current2 = current2.get_next()

    tail2 = current2

    # only true if tail1 and tail2 are the same node
    return tail1 is tail2


def intersect(head_node1, head_node2):
    """Function to check if two singly linked lists intersect.

    Args:
        head_node1 (ListNode): linkded list node containing integer value 1-9
        head_node2 (ListNode): linkded list node containing integer value 1-9

    Returns:
        intersect_node (ListNode): return None if no intersection
    """

    # check that head nodes are of type ListNode
    if not isinstance(head_node1, ListNode) or not isinstance(head_node2, ListNode):
        raise ValueError('head_node1 and head_node2 must both be ListNodes')

    # edge case - 1 node list
    if head_node1 is head_node2:
        return head_node1

    # tails must be the same node if the lists intersect
    if not tails_same(head_node1, head_node2):
        return None

    # need to know which list is longer
    longer, shorter = compare_lengths(head_node1, head_node2)

    # This should always return a node as tails matched earlier
    node_i = intersect_node(longer, shorter)

    # return the intersecting node
    return node_i

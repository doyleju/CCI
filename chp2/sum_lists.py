from linked_list import *


def sum_lists_reverse_recursive(num1, num2, carry):
    """Recursive function to add 2 numbers stored in singly linked lists

    Args:
        num1 (ListNode): node with integer value 1-9
        num2 (ListNode): node with integer value 1-9
        carry (0,1):

    Numbers are stored in reverse order.
    7 -> 1 -> 6 represents 617

    Returns:
        result (ListNode): head node holding the reverse order result
    """

    # Base case - all arguments are None or 0
    if num1 is None and num2 is None and carry == 0:
        return None

    # create a node to hold the result of adding our two values
    # Initialised with a value of 0
    result = ListNode(0, None)

    # total will hold the total value of addition
    total = carry

    if num1 is not None:
        total += num1.get_value()
    if num2 is not None:
        total += num2.get_value()

    # if the node value is > 9
    node_value = total % 10
    carry = total // 10

    # set the value of this node
    result.set_value(node_value)

    # if there is any addition left - create another node
    if num1 is not None or num2 is not None or carry == 1:
        if num1 is not None:
            num1 = num1.get_next()
        if num2 is not None:
            num2 = num2.get_next()

        next_result = sum_lists_reverse_recursive(num1, num2, carry)
        result.set_next(next_result)

    # return the result node
    return result


def sum_lists_recursive_followup_h(num1, num2):
    """Recursive helper function to add 2 numbers stored in singly linked lists

    Args:
        num1 (ListNode): linkded list node containing integer value 1-9
        num2 (ListNode): linkded list node containing integer value 1-9

    Numbers are stored in correct order.
    7 -> 1 -> 6 represents 716.
    Shorter numbers must be padded with zeros.
    e.g. to add 176, 17 add 176 to 017

    Returns:
        result (ListNode): head of the linked list holding the result
        carry (0, 1):
    """

    # Base case - all arguments are None or 0
    if num1 is None:
        return None, 0

    # total will hold the total value of addition
    total = num1.get_value() + num2.get_value()

    # get the result of adding next two numbers
    # need the carry value for this calculation
    num1, num2 = num1.get_next(), num2.get_next()
    next_result_node, carry = sum_lists_recursive_followup_h(num1, num2)

    # finalise calculations for result
    total += carry
    carry = total // 10
    value = total % 10

    # set the value of this node and link to the next result node
    result = ListNode(value, next_result_node)

    # return the result node and the carry value
    return result, carry


def pad_with_zeros(num1, num2, diff):
    """Function to pad zeros into integer singly linked list

    Args:
        num1 (SinglyLinkedList): linkded list containing integer values 1-9
        num2 (SinglyLinkedList): linkded list containing integer values 1-9
        diff (int): number of zeros needed

    7 -> 1 -> 6 represents 716. 2 -> 5 represents 25.
    Function will return 7 -> 1 -> 6 and 0 -> 2 -> 5

    Returns:
        num1 (SinglyLinkedList): linkded list containing integer values 0-9
        num2 (SinglyLinkedList): linkded list containing integer values 0-9
    """

    if len(num1) < len(num2):
        smaller = num1
    else:
        smaller = num2

    for _ in range(diff):
        smaller.prepend(0)

    return num1, num2


def sum_lists_recursive_followup(num1, num2):
    """Wrapper function to add 2 numbers stored in singly linked lists

    Args:
        num1 (SinglyLinkedList): linkded list containing integer values 1-9
        num2 (SinglyLinkedList): linkded list containing integer values 1-9

    Numbers are stored in correct order.
    7 -> 1 -> 6 represents 716.
    Recursive helper function needs numbers to be padded with zeros.
    e.g. to add 176, 17 add 176 to 017

    Returns:
        result (ListNode): head of the linked list holding the result
    """

    # Using SinglyLinkedList to simplify getting length and padding with zeros
    if not isinstance(num1, SinglyLinkedList) or not isinstance(num2, SinglyLinkedList):
        raise ValueError('num1 and num2 must both be SinglyLinkedLists')

    # if different lengths pad the smaller number with zeros
    diff = abs(len(num1) - len(num2))
    if diff:
        num1, num2 = pad_with_zeros(num1, num2, diff)

    # call the recursive helper function
    sum_head, carry = sum_lists_recursive_followup_h(num1.head(), num2.head())

    # if we have a final carry from recursive helper prepend it
    if carry == 1:
        sum_head = ListNode(1, sum_head)

    # return the result head node
    return sum_head


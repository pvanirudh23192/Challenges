from linkedlist import LinkedList

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next

node.next = loop_start

def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    # TODO: Write function to check if linked list is circular
    if linked_list.head is None:
        return False

    node_fast = linked_list.head
    node_slow = linked_list.head

    while node_fast and node_slow:
        node_fast = node_fast.next.next
        node_slow = node_slow.next

        if node_fast == node_slow:
            return True

    return False

print iscircular(list_with_loop)

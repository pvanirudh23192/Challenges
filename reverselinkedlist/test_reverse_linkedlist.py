from linkedlist import LinkedList
from node import Node

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """

    # TODO: Write your function to reverse linked lists here
    rlist = []
    reverse_list = LinkedList()
    for each in linked_list:
        rlist.append(repr(each))
    length = len(rlist)
    # for each in rlist:
    for index in range(length):
        reverse_list.append(Node(rlist.pop()))
    for each in reverse_list:
        print (repr(each))
    return (reverse_list)


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

print ("Pass" if (llist == reverse(llist)) else "Fail")

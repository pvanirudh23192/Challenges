from node import Node
from linkedlist import LinkedList
from merge import NestedLinkedList

linked_list = LinkedList(Node(1))
linked_list.append(Node(3))
linked_list.append(Node(5))

nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list.append(Node(second_linked_list))

solution = nested_linked_list.flatten()
assert solution == [1,2,3,4,5]

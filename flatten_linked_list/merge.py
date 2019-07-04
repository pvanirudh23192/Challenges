from node import Node
from linkedlist import LinkedList

def convert_to_array(list):
    current = list.head
    arr = []
    while current:
        arr.append(repr(current))
        current = current.next
    return arr

def convert_to_llist(arr):
    length = len(arr)
    llist = LinkedList(Node(arr[0]))
    for x in range(1,length):
        llist.append(Node(arr[x]))
    return llist

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    final_array = convert_to_array(list1) + convert_to_array(list2)
    final_list = convert_to_llist(sorted(final_array))

class NestedLinkedList(LinkedList):
    def flatten(self):
        print("in Flatten")
        current = self.head
        arr = []
        while current:
            if (isinstance(current.value, LinkedList)):
                arr.append(current.flatten())
            elif (isinstance(current.value, Node)):
                current = current.value
                continue
            else:
                arr.append(current.value)
                current = current.next
        return sorted(arr)#convert_to_llist(sorted(arr))



        

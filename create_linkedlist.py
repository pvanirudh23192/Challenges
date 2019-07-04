from node import Node

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    current = None
    head = None
    length = len(input_list)
    for index in range(length):
        current = Node(input_list[index])
        if head is None:
            head = current
        if index+1 < length-1:
            current.next = Node(input_list[index+1])
        current = current.next
    return head

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail 1")
                return
        for value in input_list:
            print (head.value)
            if head.value != value:
                print("Fail 2")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + str(e))



input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

# input_list = [1]
# head = create_linked_list(input_list)
# test_function(input_list, head)
#
# input_list = []
# head = create_linked_list(input_list)
# test_function(input_list, head)

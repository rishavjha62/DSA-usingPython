# LL : Find Kth Node from End without using length(** Interview Question)

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
# writing the find_kth_from_end function

def find_kth_from_end(alist, n):
    slow = alist.head
    fast = alist.head

    for i in range(n):
        if fast is None:
            return None
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
    return slow      
        
        
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)  # Output : 4



""" 
    Expected Output : 4    
"""

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append_list(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_list(self):
        if self.length == 0:
            return None
        pre = self.head
        post = self.head
        while post.next is not None:
            pre = post
            post = post.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return post
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            

my_linked_list = LinkedList(1)
my_linked_list.append_list(2)

# (2) Items- Returns Node 2
print(my_linked_list.pop_list())
# (1) Item - Returns 1 Node
print(my_linked_list.pop_list())
# (0) Item - Returns None
print(my_linked_list.pop_list())


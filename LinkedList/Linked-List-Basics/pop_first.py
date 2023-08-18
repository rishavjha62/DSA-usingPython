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
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            

my_linked_list = LinkedList(2)
my_linked_list.append_list(3)
my_linked_list.prepend(1)

print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())


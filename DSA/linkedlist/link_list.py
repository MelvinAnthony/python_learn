class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
l1 = link_list()
l1.append(10)
l1.append(20)
l1.append(30)


# Print linked list
current = l1.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
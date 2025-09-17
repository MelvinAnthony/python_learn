class node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = node(10)
n2 = node(20)
n3 = node(30)


n1.next = n2 
n2.next = n3

current = n1

while current.next:
    current = current.next
print(current.data)


print(new_world)
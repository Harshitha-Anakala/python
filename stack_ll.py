class node:
    def __init__(self, data):
        self.data = data
        self.add = None

class ll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newnode = node(data)
        if self.head is None:  
            self.head = newnode
            self.tail = newnode
        else:  
            self.tail.add = newnode
            self.tail = newnode

def display_reverse(head):
    if head is None:  
        return
    display_reverse(head.add) 
    print(head.data, end=" ")  
obj = ll()
n = int(input())
while n > 0:
    obj.insert(n)
    n = int(input())

print()
display_reverse(obj.head)

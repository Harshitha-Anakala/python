class Node:
    def __init__(self, data):
        self.data = data 
        self.add = None   

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def insert(self, data):
        newnode = Node(data)  
        if self.head is None:
            self.head = newnode  
            self.tail = newnode
        else:
            self.tail.add = newnode  
            self.tail = newnode       

    def display(self):
        current = self.head 
        while current is not None:  
            print(current.data)  
            current = current.add  
obj = LinkedList()
n = int(input("Enter numbers to insert (negative number to stop): "))

while True:
    if n > 0:
        obj.insert(n) 
        n = int(input("Enter the next number: ")) 
    else:
        break

print("Linked List Before Display:")
obj.display() 

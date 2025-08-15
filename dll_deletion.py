class Node:
    def __init__(self, data):
        self.data = data 
        self.add = None   
        self.next=None

class ll:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def insert(self, data):
        newnode = Node(data)  
        if self.head is None:
            self.head = newnode  
            self.tail = newnode
        else:
            self.tail.next = newnode 
            newnode.prev=self.tail 
            self.tail = newnode       

    def display(self):
        current = self.head 
        while current is not None:  
            print(current.data)  
            current = current.add 
                
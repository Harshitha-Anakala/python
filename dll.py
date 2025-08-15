class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    '''def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode'''
    def insert_at_start(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.prev=newnode
            newnode.next = self.head
            self.head = newnode
            self.tail=newnode

    def display(self):
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.next
obj=dll()
n=int(input())
while True:
    if n>0:
        obj.insert_at_start(n)
        n=int(input())
    else:
        break
obj.display()
            
        
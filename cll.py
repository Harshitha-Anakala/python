class node:
    def __init__(self,data):
        self.data=data
        self.add=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.add=self.head
        else:
            self.tail.add=newnode
            newnode.add=self.head
            self.tail=newnode     
    def display(self):
        temp=self.head
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.add
            if temp ==self.head:
                break
obj=cll()
n=int(input())
while True:
    if n>0:
        obj.insert(n)
        n=int(input())
    else:
        break
obj.display()
        
        
        

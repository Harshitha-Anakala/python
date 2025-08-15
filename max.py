class node:
    def __init__(self, data):
        self.data=data
        self.add=None
class ll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.add=newnode
            self.tail=newnode
    def display(self):
        t = []
        while self.head is not None:
            t.append(self.head.data)
            self.head = self.head.add
        print( max(t))
obj=ll()
n=int(input())
while True:
    if n>0:
        obj.insert(n)
        n=int(input())
    else:
        break
obj.display()

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if not data:
            return
        
        queue = []
        self.root = node(data[0])
        queue.append(self.root)
        i = 1
        while queue and i < len(data):
            parent = queue.pop(0)
            
            leftvalue = data[i]
            if leftvalue != -1:
                parent.left = node(leftvalue)
                queue.append(parent.left)
            i += 1
            
            if i < len(data):
                rightvalue = data[i]
                if rightvalue != -1:
                    parent.right = node(rightvalue)
                    queue.append(parent.right)
                i += 1
    '''def levelorder(self, root):
        if root is None:
            return
        Q = []
        Q.append(root)
        while Q:
            cur = Q.pop(0)
            print(cur.data)
            if cur.left:
                Q.append(cur.left)
            if cur.right:
                Q.append(cur.right)'''
                
    '''def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)'''
        
    def countnode(self,root):
        if root is None:
            return 0
        return self.countnode(root.left)+self.countnode(root.right)+1
    
    '''def preorder(self,root):
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
        
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=' ')'''

input_data = list(map(int, input().split()))
object = tree()
object.insert(input_data)
#object.preorder(object.root)
#object.postorder(object.root)
object.countnode(object.root)
print(object.countnode(object.root))

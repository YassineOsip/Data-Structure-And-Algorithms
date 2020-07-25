class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
      if not self.root: # self.root = None
        self.root = Node(val)
      else:
        node = self.root
        while True:
          if node.info > val:
            if node.left:
              node = node.left
            else:
              # node.left == None
              node.left = Node(val)
              break
          else:
            if node.right:
              node = node.right
            else:
              node.right = Node(val)
              break

# some tests

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

# simple example using stdin and stdout
#input> 8
#input> 8 4 9 1 2 3 6 5
#output> 8 4 1 2 3 6 5 9
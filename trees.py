from queue import Queue

# simple implementation of a tree structure 
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None
    
    @classmethod
    def with_children(cls, val, left=None, right=None):
      node = cls(val)
      node.left = left
      node.right = right
      return node

    def __str__(self):
        return str(self.info)


#count tree height
def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))

# show nodes in top_view node
def top_view(root):
  level_to_node = {}
  q = Queue()
  q.put((root, 0))
  while not q.empty():
    node, level = q.get()
    if not node:
      continue

    if level not in level_to_node:
      level_to_node[level] = node.info

    q.put((node.left, level - 1))
    q.put((node.right, level + 1))

  return level_to_node
  
# Building the tree
node14 = Node.with_children(14)
node11 = Node.with_children(11, right=node14)
node8, node6, node10 = Node.with_children(8), Node.with_children(6, node11), Node.with_children(10)
node20, node7 = Node.with_children(20, node8), Node.with_children(7, node6, node10)
node12 = Node.with_children(12, left=node20, right=node7)
root = node12

#some tests

## height function tests
assert height(root) == 4
print(f"Tree with root 12 has height 4")
assert height(node14) == 0
print(f"Subtree with root 14 has height 0")
assert height(node20) == 1
print(f"Subtree with root 20 has height 1")

print(f"###################################################3")

## top_view function tests
level_to_node = top_view(root)
print(' -> '.join([str(node_val) for _, node_val in sorted(level_to_node.items())]))
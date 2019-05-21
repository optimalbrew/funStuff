"""
Preorder, inorder and postorder binary tree traversals using recursion:
"""

class TreeNode:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x

# Nodes    
A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F') #root
G = TreeNode('G')
H = TreeNode('H')
I = TreeNode('I') 

# Define the Shape
"""
                 F
              /     \ 
            B         G
          /   \        \    
        A       D        I
               / \      /
              C   E    H

"""

root = F
root.left = B
root.right = G
B.left = A
B.right = D
D.left = C
D.right = E
G.right = I
I.left = H

# inorder traversal of the tree
def inorderTrav(root):
    nodes = [] #to keep track of traversed nodes
    prev = [root] #to keep track of previous nodes to return to    
    if root.left != None:
        inorderTrav(root.left)
    nodes.append(root.val)
    print(nodes)
    if root.right != None:
        inorderTrav(root.right)
    root = prev.pop()
    

# preorder traversal of the tree
def preorderTrav(root):
    nodes = [] #to keep track of traversed nodes
    prev = [root] #to keep track of previous nodes to return to    
    nodes.append(root.val)
    print(nodes)
    if root.left != None:
        preorderTrav(root.left)
    if root.right != None:
        preorderTrav(root.right)
    root = prev.pop()



# postorder traversal of the tree
def postorderTrav(root):
    nodes = [] #to keep track of traversed nodes
    prev = [root] #to keep track of previous nodes to return to    
    if root.left != None:
        postorderTrav(root.left)
    if root.right != None:
        postorderTrav(root.right)
    nodes.append(root.val)
    print(nodes)
    root = prev.pop()


inorderTrav(root)

preorderTrav(root)    

postorderTrav(root)



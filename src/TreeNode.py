"""
Working with trees
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

# Shape
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
    nodes = []
    while root.left != None:



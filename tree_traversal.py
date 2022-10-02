# Definition for a binary tree node.
# Depth First Traversals: 
#(a) Inorder (Left, Root, Right) 
#(b) Preorder (Root, Left, Right)  
#(c) Postorder (Left, Right, Root) 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root_val:TreeNode=None):
        self.root = root_val # This is the head

def traverse_tree(node: TreeNode):
    if node is not None:
        traverse_tree(node.left)
        traverse_tree(node.right)
        print(f"{node.val}->", end=" ")  # 0

# def recursive(tree: TreeNode):

root = TreeNode(0, 
        TreeNode(1, TreeNode(2), TreeNode(3)), 
        TreeNode(4, TreeNode(5), TreeNode(6))
        )
traverse_tree(root)


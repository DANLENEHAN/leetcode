# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Binary Tree PostOrder Traversal
class Solution(object):
    def postorderTraversal(self, root):

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        visited = []
        visited += self.postorderTraversal(root.left)
        visited += self.postorderTraversal(root.right)

        visited += [root.val]

        return visited


# Binary Tree PreOrder Traversal
class Solution(object):
    def preorderTraversal(self, root):

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        visited = []
        visited += [root.val]
        visited += self.preorderTraversal(root.left)
        visited += self.preorderTraversal(root.right)
        
        return visited


# Binary Tree Inorder Traversal
class Solution(object):
    def inorderTraversal(self, root):

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        visited = []
        visited += self.inorderTraversal(root.left)
        visited += [root.val]
        visited += self.inorderTraversal(root.right)

        return visited

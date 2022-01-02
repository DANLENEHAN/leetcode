
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        visted = []
        node = root

        while node:
            if node not in visted:
                visted.append(node)
            if (
                node.left is not None and
                node.left not in visted
            ):
                stack.append(node)
                node = node.left
            elif (
                node.right is not None and
                node.right not in visted
            ):
                stack.append(node)
                node = node.right
            else:
                if stack != []:
                    node = stack.pop()
                else:
                    node = None
        return [node.val for node in visted]


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        visted = []
        node = root

        while node:
            if (
                node.left is not None and
                node.left not in visted
            ):
                stack.append(node)
                node = node.left
            elif (
                node.right is not None and
                node.right not in visted
            ):
                if node not in visted:
                    visted.append(node)
                stack.append(node)
                node = node.right
            else:
                if node not in visted:
                    visted.append(node)
                if stack != []:
                    node = stack.pop()
                    if node not in visted:
                        visted.append(node)
                else:
                    node = None
        return [node.val for node in visted]


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        visted = []
        node = root

        while node:
            if (
                node.left is not None and
                node.left not in visted
            ):
                stack.append(node)
                node = node.left
            elif (
                node.right is not None and
                node.right not in visted
            ):
                stack.append(node)
                node = node.right
            else:
                if node not in visted:
                    visted.append(node)
                if stack != []:
                    node = stack.pop()
                else:
                    node = None
        return [node.val for node in visted]
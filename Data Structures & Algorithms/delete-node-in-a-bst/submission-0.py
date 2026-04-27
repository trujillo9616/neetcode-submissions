# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minLeftmostNode(self, root):
        node = root
        while node and node.left:
            node = node.left
        return node

    # Remove a node and return the root of the BST.
    def deleteNode(self, root, val):
        if not root:
            return None
        
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
        elif val < root.val:
            root.left = self.deleteNode(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minLeftmostNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
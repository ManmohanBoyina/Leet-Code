# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        if left is None and right is None:
            return 1
        if root.left==None:
            return right+1
        if root.right==None:
            return left+1
        return 1+min(left,right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.maxDepth(root)!=-1
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(minval,maxval,root):
            if root is None:
                return True
            if not(minval<root.val<maxval):
                return False
            return validate(minval,root.val,root.left) and validate(root.val,maxval,root.right)
        return validate(float('-inf'),float('inf'),root)
        
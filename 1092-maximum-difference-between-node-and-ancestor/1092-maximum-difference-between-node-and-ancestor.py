# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def help(root,cmin,cmax):
            if not root:
                return cmax-cmin
            cmax=max(cmax,root.val)
            cmin=min(cmin,root.val)
            left=help(root.left,cmin,cmax)
            right=help(root.right,cmin,cmax)
            return max(left,right)
        return help(root,root.val,root.val)

        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(root,values):
            if root:
                inorder(root.left,values)
                values.append(root.val)
                inorder(root.right,values)
        values=[]
        inorder(root,values)
        return values[k-1]
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
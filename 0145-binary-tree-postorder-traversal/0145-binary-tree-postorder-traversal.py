# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.result(root,ans)
        return ans
    def result(self,root,ans):
        if not root:
            return
        self.result(root.left,ans)
        self.result(root.right,ans)
        ans.append(root.val)
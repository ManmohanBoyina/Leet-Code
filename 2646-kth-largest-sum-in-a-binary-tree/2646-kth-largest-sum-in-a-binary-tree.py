# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        queue=deque([root])
        res=[]
        while queue:
            clevel=len(queue)
            summ=0
            for _ in range(clevel):
                node=queue.popleft()
                summ+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(summ)
        if len(res)<k:
            return -1
        res.sort()
        return res[-k]
        
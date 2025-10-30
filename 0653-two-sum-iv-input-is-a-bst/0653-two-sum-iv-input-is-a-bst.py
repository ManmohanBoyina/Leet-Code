# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        queue=deque([root])
        dicto=set()
        while queue:
            current=queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if k-current.val in dicto:
                return True
            else:
                dicto.add(current.val)
        return False
            

        
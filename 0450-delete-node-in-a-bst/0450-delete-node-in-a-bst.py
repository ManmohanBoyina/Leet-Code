# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val==key:
            return self.connector(root)
        node=root
        while node:
            if node.val>key:
                if node.left and node.left.val==key:
                    node.left=self.connector(node.left)
                else:
                    node=node.left
            elif node.val<key:
                if node.right and node.right.val==key:
                    node.right=self.connector(node.right)
                else:
                    node=node.right
        return root
    def connector(self,root):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        leftnode=root.left
        lmost=root.right
        while lmost.left:
            lmost=lmost.left
        lmost.left=leftnode
        return root.right

        
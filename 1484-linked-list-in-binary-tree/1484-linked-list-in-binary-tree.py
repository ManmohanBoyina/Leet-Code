class Solution(object):
    def checkPath(self, head, root):
        if not head:
            return True
        if not root or head.val != root.val:
            return False
        return self.checkPath(head.next, root.left) or self.checkPath(head.next, root.right)

    def isSubPath(self, head, root):
        if not root:
            return False
        return (head.val == root.val and self.checkPath(head, root)) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)      
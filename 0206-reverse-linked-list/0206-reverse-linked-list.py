# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        s=[]
        cur=head
        t=head
        while cur:
            t=cur.next
            cur.next=prev
            prev=cur
            cur=t
        return prev
        
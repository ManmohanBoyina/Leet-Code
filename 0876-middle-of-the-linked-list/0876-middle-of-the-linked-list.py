# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        first=head
        second=head
        while (second!=None and second.next!=None):
            first=first.next
            second=second.next.next
        return first
        
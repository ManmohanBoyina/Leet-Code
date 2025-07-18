# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        c1=head
        c2=prev
        maxi = float('-inf')
        while c2:
            maxi = max(maxi, c1.val + c2.val)
            c1 = c1.next
            c2 = c2.next
        return maxi
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(current):
            if current is None or current.next is None:
                return current
            current.val, current.next.val = current.next.val, current.val
            swap(current.next.next)
        swap(head)
        return head

        
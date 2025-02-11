# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.next
                while temp and temp.val == curr.val:
                    temp = temp.next
                if prev:
                    prev.next = temp
                else:
                    head = temp
                curr = temp
            else:
                prev = curr
                curr = curr.next
        return head
        
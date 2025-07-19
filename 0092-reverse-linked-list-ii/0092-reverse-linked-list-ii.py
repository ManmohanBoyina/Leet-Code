# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        curr = head
        start = end = front = last = None
        while count != left:
            front = curr
            curr = curr.next
            count += 1
        start = curr
        while count != right:
            curr = curr.next
            count += 1
        end = curr
        last = end.next
        prev = None
        c1 = start
        while True:
            next_node = c1.next
            c1.next = prev
            prev = c1
            if c1 == end:
                break
            c1 = next_node
        if front:
            front.next = end
        else:
            head = end
        start.next = last
        return head
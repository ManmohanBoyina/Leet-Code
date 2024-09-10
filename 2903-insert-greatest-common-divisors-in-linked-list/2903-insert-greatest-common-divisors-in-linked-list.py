# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(a, b):
        if(b == 0):
            return abs(a)
        else:
            return gcd(b, a % b)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        temp1=head.next
        while temp1!=None:
            v=gcd(temp.val,temp1.val)
            New_node=ListNode(v)
            temp.next=New_node
            New_node.next=temp1
            temp=temp.next.next
            temp1=temp1.next
        return head
        
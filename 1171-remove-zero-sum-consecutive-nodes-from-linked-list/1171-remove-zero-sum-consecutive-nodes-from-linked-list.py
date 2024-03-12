# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        a={}
        sum=0
        d=ListNode(0)
        d.next=head
        a[0]=d
        while head:
            sum+=head.val
            if sum in a:
                s=a[sum]
                temp=s
                ps=sum
                while temp!=head:
                    temp=temp.next
                    ps+=temp.val
                    if temp!=head:
                        del a[ps]
                s.next=head.next
            else:
                a[sum]=head
            head=head.next
        return d.next
        
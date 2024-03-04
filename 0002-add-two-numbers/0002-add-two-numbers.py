# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s=''
        s1=''
        while l1.next!=None:
            s=s+str(l1.val)
            l1=l1.next
        while l2.next!=None:
            s1=s1+str(l2.val)
            l2=l2.next
        s=s+str(l1.val)
        s1=s1+str(l2.val)
        s1=s1[::-1]
        s=s[::-1]
        a=int(s)+int(s1)
        b=str(a)
        c=[]
        b=b[::-1]
        c=[int(i) for i in b]
        o=ListNode()
        h=o
        h.val=c[0]
        for i in range(1,len(c)):
            n=ListNode()
            n.val=c[i]
            h.next=n
            h=h.next
        return o



            

        
# Definition for singly-linked list.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        if length-n==0:
            return head.next
        temp = head
        for _ in range(length-n-1):
            temp = temp.next
        temp.next = temp.next.next

        return head
        

        
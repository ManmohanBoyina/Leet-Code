# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self,head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
        
    def getKthNode(self,temp,k):
        k-=1
        while k!=0 and temp!=None:
            temp=temp.next
            k-=1
        return temp
    def reverseKGroup(self, head, k):
        temp = head
        prevLast = None
        while temp is not None:
            kThNode = self.getKthNode(temp, k)
            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break
            nextNode = kThNode.next
            kThNode.next = None
            self.reverseLinkedList(temp)
            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode
            prevLast = temp
            temp = nextNode
        return head
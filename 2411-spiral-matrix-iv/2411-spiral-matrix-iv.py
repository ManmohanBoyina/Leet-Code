# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        a=[[ 0 for _ in range (n)] for _ in range (m)]
        left,right=0,n-1
        top,bottom=0,m-1
        leng=m*n
        count,val=0,0
        while count<leng:
            #top row
            for row in range(left,right+1):
                if count >= leng:
                    break
                if head!=None:
                    val=head.val
                    head=head.next
                else:
                    val=-1
                a[top][row]=val
                count+=1
            top+=1
            #left column
            for column in range(top,bottom+1):
                if count >= leng:
                    break
                if head!=None:
                    val=head.val
                    head=head.next
                else:
                    val=-1
                a[column][right]=val
                count+=1
            right-=1
            #bottom row
            for column in range(right,left-1,-1):
                if count >= leng:
                    break
                if head!=None:
                    val=head.val
                    head=head.next
                else:
                    val=-1
                a[bottom][column]=val
                count+=1
            bottom-=1
            #right row
            for column in range(bottom,top-1,-1):
                if count >= leng:
                    break
                if head!=None:
                    val=head.val
                    head=head.next
                else:
                    val=-1
                a[column][left]=val
                count+=1
            left+=1
        return a
        
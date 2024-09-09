class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0]* n for _ in range(n)]
        left,right=0,n-1
        top,bottom=0,n-1
        val=1
        while left<=right:
            #Top Row
            for column in range(left,right+1):
                ans[top][column]=val
                val+=1
            top+=1
            #Right column
            for row in range(top,bottom+1):
                ans[row][right]=val
                val+=1
            right-=1
            #bottom row(reverse)
            for column in range(right,left-1,-1):
                ans[bottom][column]=val
                val+=1
            bottom-=1
            #left column
            for row in range(bottom,top-1,-1):
                ans[row][left]=val
                val+=1
            left+=1
        return ans
            
        
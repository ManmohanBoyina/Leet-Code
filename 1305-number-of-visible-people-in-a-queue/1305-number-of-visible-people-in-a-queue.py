class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans=[0]*len(heights)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            height=heights[i]
            count=0
            while stack and height>stack[-1]:
                count+=1
                stack.pop()
            if stack:
                count+=1
            stack.append(heights[i])
            ans[i]=count
        return ans


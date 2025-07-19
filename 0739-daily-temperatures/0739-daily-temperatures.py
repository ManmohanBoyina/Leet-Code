from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[]
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            if stack:
                ans.append(abs(i-stack[-1][1]))
            else:
                ans.append(0)
            stack.append([temperatures[i],i])
        return ans[::-1]
        
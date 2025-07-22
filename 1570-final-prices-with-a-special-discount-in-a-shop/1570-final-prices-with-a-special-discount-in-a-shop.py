from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = []
        arr = list(reversed(prices))
        for i in range(len(arr)):
            disc = 0
            while stack and stack[-1] > arr[i]:
                stack.pop()
            if stack:
                disc = stack[-1]
            ans.append(arr[i] - disc)
            stack.append(arr[i])
        ans.reverse()
        return ans
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        ans=0
        for right in range(1,len(prices)):
            if prices[left]>prices[right]:
                left=right
            else:
                diff=prices[right]-prices[left]
                ans=max(diff,ans)
        return ans
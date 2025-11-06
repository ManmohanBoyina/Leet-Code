class Solution(object):
    def maxProfit(self, nums):
        buy=nums[0]
        max_profit=0
        for i in range(1,len(nums)):
            if nums[i]<buy:
                buy=nums[i]
            else:
                profit=nums[i]-buy
                max_profit=max(max_profit,profit)
        return max_profit

class Solution(object):
    def maxProfit(self, nums):
        buy=nums[0]
        total=0
        for i in range(1,len(nums)):
            if buy>nums[i]:
                buy=nums[i]
            else:
                total+=(nums[i]-buy)
                print(nums[i]-buy)
                if i<len(nums)-1:
                    buy=nums[i]
                else:
                    return total
        return total
class Solution(object):
    def partitionArray(self, nums, k):
        ans=1
        nums.sort()
        rec=nums[0]
        for i in nums:
            if i-rec>k:
                ans+=1
                rec=i
        return ans

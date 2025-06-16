from collections import Counter
class Solution(object):
    def maximumDifference(self, nums):
        mini=nums[0]
        maxi=-1
        for i in range(1,len(nums)):
            res=nums[i]-mini
            if res>0:
                maxi=max(maxi,res)
            if mini>nums[i]:
                mini=nums[i]
        return maxi



        
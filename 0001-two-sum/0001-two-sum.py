class Solution(object):
    def twoSum(self, nums, target):
        a={}
        for i in range(len(nums)):
            t=nums[i]
            temp=target-t
            if temp in a:
                return [a[temp],i]
            a[t]=i
        return -1,-1
        
class Solution(object):
    def twoSum(self, nums, target):
        c=[]
        x=len(nums)
        for i in range(x-1):
            for j in range(i+1,x):
                if nums[i]+nums[j]==target:
                    c.append(i)
                    c.append(j)
        return c
        
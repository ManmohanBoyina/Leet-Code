class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        a=(n*(n+1))//2
        b=sum(nums)
        return a-b
        
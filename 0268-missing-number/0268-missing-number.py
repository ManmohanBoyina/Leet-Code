class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        tsum=(n*(n+1))//2
        psum=0
        for i in range(n):
            psum+=nums[i]
        return tsum-psum

        
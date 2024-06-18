class Solution:
    def maxProduct(self, nums):
        p,s=1,1
        ans=float('-inf')
        for i in range(len(nums)):
            if p==0:
                p=1
            if s==0:
                s=1
            p=p*nums[i]
            s=s*nums[len(nums)-i-1]
            ans=max(ans,max(p,s))
        return ans

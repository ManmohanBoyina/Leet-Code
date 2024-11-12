class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans,sum=0,0
        for i in range(len(nums)):
            sum+=nums[i]
            ans=min(ans,sum)
        return -ans+1
        
        
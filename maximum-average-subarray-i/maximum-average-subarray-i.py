class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=0
        for i in range(k):
            c+=nums[i]
        ans=c
        for i in range(k,len(nums)):
            c+=nums[i]-nums[i-k]
            ans=max(ans,c)
        return ans/k
        
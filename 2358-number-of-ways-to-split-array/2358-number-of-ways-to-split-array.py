class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total=sum(nums)
        ans=0
        left=0
        for i in range(len(nums)-1):
            left+=nums[i]
            right=total-left
            if left>=right:
                ans+=1
        return ans

        return 0

        
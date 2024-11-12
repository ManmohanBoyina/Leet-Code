class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            prefix.append(sum)
        ans=0
        for i in range(len(prefix)-1):
            left=prefix[i]
            right=prefix[-1]-prefix[i]
            if left>=right:
                ans+=1
        return ans

        return 0

        
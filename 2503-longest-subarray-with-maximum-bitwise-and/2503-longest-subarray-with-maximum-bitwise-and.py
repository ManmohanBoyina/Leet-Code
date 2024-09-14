class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value=0
        for i in range(len(nums)):
            max_value=max(max_value,nums[i])
        res,c=0,0
        for i in range(len(nums)):
            if nums[i]==max_value:
                c+=1
            else:
                c=0
            res=max(res,c)
        return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            ref=target-nums[i]
            if ref in a:
                return [a[ref],i]
            a[nums[i]]=i
        
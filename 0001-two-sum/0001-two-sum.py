class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reference={}
        for i in range(len(nums)):
            ref=target-nums[i]
            if ref in reference:
                return [reference[ref],i]
            reference[nums[i]]=i
        return [-1,-1]
        
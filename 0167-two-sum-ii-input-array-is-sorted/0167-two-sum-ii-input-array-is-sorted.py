class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left,right=0,len(nums)-1
        while left<right:
            ans=nums[left]+nums[right]
            if ans==target:
                return [left+1,right+1]
            elif ans>target:
                right-=1
            else:
                left+=1
        return [-1,-1]

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        a={}
        left=0
        maxi=-1
        for right in range(len(nums)):
            if nums[right] not in a:
                a[nums[right]]=1
            else:
                a[nums[right]]+=1
            while a[nums[right]]>k and left<right:
                a[nums[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi
        
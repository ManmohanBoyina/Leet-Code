class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        a={}
        left,summ,maxi=0,0,0
        for right in range(len(nums)):
            if nums[right] not in a:
                a[nums[right]]=1
            else:
                a[nums[right]]+=1
            while a[nums[right]]>1:
                a[nums[left]]-=1
                left+=1
            summ=sum(nums[left:right+1])
            maxi=max(summ,maxi)
        return maxi
        
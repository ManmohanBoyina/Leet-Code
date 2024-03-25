class Solution(object):
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        mini=sys.maxsize
        while left<=right:
            mid=(left+right)//2
            if nums[left]<=nums[right]:
                mini=min(mini,nums[left])
                break
            if nums[left]<=nums[mid]:
                mini=min(mini,nums[left])  
                left=mid+1
            else:
                mini=min(mini,nums[mid])
                right=mid-1
        return mini
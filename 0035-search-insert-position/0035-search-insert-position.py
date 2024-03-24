class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        ind=0
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    ind=mid
                else:
                    ind=mid+1
                low=mid+1
            else:
                high=mid-1
        return ind

        
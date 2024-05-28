class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1
            
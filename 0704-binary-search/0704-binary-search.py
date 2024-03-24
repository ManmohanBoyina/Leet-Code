class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while(left<=right):
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            left+=1
            right-=1
        return -1
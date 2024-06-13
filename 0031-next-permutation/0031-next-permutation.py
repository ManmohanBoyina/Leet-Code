class Solution(object):
    def nextPermutation(self, nums):
        t=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                t=i
                break
        if t==-1:
            nums=nums.reverse()
            return nums
        for i in range(len(nums)-1,t,-1):
            if nums[i]>nums[t]:
                nums[i],nums[t]=nums[t],nums[i]
                break
        nums[t+1:] = reversed(nums[t+1:])
        return nums



        
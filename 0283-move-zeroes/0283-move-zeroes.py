class Solution(object):
    def moveZeroes(self, nums):
        j=-1
        for i in range (len(nums)):
            if nums[i]==0:
                j=i
                break
        for i in range(j+1,len(nums)):
            if nums[i]!=0 and nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                j=j+1
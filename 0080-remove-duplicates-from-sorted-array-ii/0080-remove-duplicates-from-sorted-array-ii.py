class Solution(object):
    def removeDuplicates(self, nums):
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-1]:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
            elif nums[i]!=nums[k-2]:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
        return k
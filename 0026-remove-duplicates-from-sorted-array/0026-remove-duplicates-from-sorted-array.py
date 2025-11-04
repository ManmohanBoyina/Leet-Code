class Solution(object):
    def removeDuplicates(self, nums):
        k=1
        temp=nums[0]
        for i in range(len(nums)):
            if temp==nums[i]:
                continue
            else:
                nums[k]=nums[i]
                k+=1
                temp=nums[i]
        return k
        
class Solution(object):
    def removeDuplicates(self, nums):
        fp=0
        sp=1
        while sp!=len(nums):
            if nums[fp]!=nums[sp]:
                nums[fp+1]=nums[sp]
                fp=fp+1
            sp=sp+1
        return fp+1
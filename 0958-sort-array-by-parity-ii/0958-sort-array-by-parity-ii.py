class Solution(object):
    def sortArrayByParityII(self, nums):
        even,odd=0,1
        while even<len(nums) and odd<len(nums):
            if nums[even]%2==1 and nums[odd]%2==0:
                nums[even],nums[odd]=nums[odd],nums[even]
            elif nums[even]%2==0:
                even+=2
            elif nums[odd]%2==1:
                odd+=2
        return nums 
        
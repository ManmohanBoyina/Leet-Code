class Solution(object):
    def majorityElement(self, nums):
        count=0
        num=nums[0]
        for i in range(len(nums)):
            if count==0:
                num=nums[i]
            if num==nums[i]:
                count+=1
            elif num!=nums[i]:
                count-=1
        count=0
        for i in range(len(nums)):
            if nums[i]==num:
                count+=1
        if count>=len(nums)//2:
            return num

        
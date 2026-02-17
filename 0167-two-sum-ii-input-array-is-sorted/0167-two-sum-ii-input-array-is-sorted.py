class Solution(object):
    def twoSum(self, nums, target):
        i,j=0,len(nums)-1
        while i<j:
            temp=nums[i]+nums[j]
            if temp>target:
                j-=1
            elif temp<target:
                i+=1
            else:
                return [i+1,j+1]
                
        
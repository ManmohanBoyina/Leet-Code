class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        ans=[]
        for i in range(0,len(nums)-2,3):
            if nums[i+2]-nums[i]>k:
                return []
            ans.append(nums[i:i+3])
        return ans
        
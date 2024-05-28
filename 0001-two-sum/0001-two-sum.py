class Solution(object):
    def twoSum(self, nums, target):
        mpp = {}
        for i in range(len(nums)):
            num = nums[i]
            more_needed = target - num
            if more_needed in mpp:
                return [mpp[more_needed], i]
            mpp[num] = i
        return [-1, -1]
        
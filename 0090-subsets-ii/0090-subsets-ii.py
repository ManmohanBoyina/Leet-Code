class Solution:
    def subsetsWithDup(self, nums):
        resl = []
        nums.sort()
        self.result(nums, [], 0, resl)
        return resl
    
    def result(self, nums, res, ind, resl):
        resl.append(res[:])
        
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            res.append(nums[i])
            self.result(nums, res, i + 1, resl)
            res.pop()

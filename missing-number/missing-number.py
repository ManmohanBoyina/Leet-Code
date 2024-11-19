class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a={}
        for ind,val in enumerate(nums):
            a[val]=ind
        for i in range(len(a)):
            if i not in a:
                return i
        return len(a)
        
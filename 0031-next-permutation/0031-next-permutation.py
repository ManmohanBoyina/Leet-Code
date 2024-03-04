class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        bp=-1
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                bp=i
                break
        if bp==-1:
            nums=nums.reverse()
        else:
            for i in range(n-1,bp,-1):
                if nums[i]>nums[bp]:
                    nums[i],nums[bp]=nums[bp],nums[i]
                    break
            nums[bp+1:] = reversed(nums[bp+1:])

        
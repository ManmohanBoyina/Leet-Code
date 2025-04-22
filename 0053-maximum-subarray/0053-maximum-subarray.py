class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0
        left,right=0,0
        maxi=-1
        while right!=len(nums):
            summ+=nums[right]
            while summ<0:
                summ-=nums[left]
                left+=1
            maxi=max(summ,maxi)
            right+=1
        return maxi if maxi>0 else max(nums)

        
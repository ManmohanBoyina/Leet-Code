class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        left=0
        right=len(nums)-1
        n=len(nums)-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                a[n]=nums[left]*nums[left]
                left+=1
            else:
                a[n]=nums[right]*nums[right]
                right-=1
            n-=1
        return a
                
        
        
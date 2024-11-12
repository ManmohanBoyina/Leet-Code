class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        avg=[-1]*n
        radius=k*2+1
        if k==0:
            return nums
        if radius>n:
            return avg
        wsum=sum(nums[:radius])
        avg[k]=wsum//radius
        for i in range(radius,n):
            wsum=wsum-nums[i-radius]+nums[i]
            avg[i-k]=wsum//radius
        return avg
        
        
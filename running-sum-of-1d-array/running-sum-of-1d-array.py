class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        sum=0
        for i in nums:
            sum+=i
            a.append(sum)
        return a
        
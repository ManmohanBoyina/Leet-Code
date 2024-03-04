class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            if a[i]==1:
                return int(i)
        
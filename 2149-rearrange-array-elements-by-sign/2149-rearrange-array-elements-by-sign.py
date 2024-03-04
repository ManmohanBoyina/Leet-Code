class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[0]*n
        p,ng=0,1
        for i in nums:
            if i>0:
                a[p]=i
                p+=2
            else:
                a[ng]=i
                ng+=2
        return a

        
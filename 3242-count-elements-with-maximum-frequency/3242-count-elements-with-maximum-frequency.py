class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a={}
        maxi=0
        for i in nums:
            if i in a:
                a[i]+=1
                maxi=max(maxi,a[i])
            else:
                a[i]=1
                maxi=max(maxi,a[i])
        c=0
        for i in a.keys():
            if a[i]==maxi:
                c+=1
        return c*maxi
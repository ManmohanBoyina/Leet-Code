from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        a=Counter(nums)
        maxi=-1
        for i in a.keys():
            if a[i]==1:
                maxi=max(maxi,i)
        return maxi
            
        
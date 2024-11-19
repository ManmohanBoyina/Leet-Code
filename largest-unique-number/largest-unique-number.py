from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        a=Counter(nums)
        maxi=float('-inf')
        for i in a.keys():
            if a[i]==1:
                maxi=max(maxi,i)
        return -1 if maxi==float('-inf') else maxi
            
        
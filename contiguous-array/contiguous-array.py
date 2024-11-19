from collections import Counter
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        maxi=0
        pm={0:-1}
        for i in range(len(nums)):
            count+=1 if nums[i]==1 else -1
            if count in pm:
                maxi=max(maxi,i-pm[count])
            else:
                pm[count]=i
        return maxi
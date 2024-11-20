from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum=0
        a=Counter(nums)
        print(a)
        for i in a.keys():
            if a[i]==1:
                sum+=i
        return sum
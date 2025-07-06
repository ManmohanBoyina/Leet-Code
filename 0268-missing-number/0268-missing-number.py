class Solution(object):
    def missingNumber(self, nums):
        count=collections.Counter(nums)
        temp=0
        for i in range(len(nums)):
            if temp in count.keys():
                temp+=1
            else:
                return temp
        return temp

        
class Solution(object):
    def containsDuplicate(self, nums):
        ans={}
        for i in nums:
            if i in ans:
                return True
            ans[i]=1
        return False
        
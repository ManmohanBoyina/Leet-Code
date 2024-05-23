class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m1,m2=0,0
        for i in nums:
            if i==1:
                m1=m1+1
            else:
                m1=0
            m2=max(m1,m2)
        return m2
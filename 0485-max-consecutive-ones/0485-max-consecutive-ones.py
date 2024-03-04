class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=nums
        b=[]
        c=0
        for i in range(len(a)):
            if(a[i]==0):
                b.append(c)
                c=0
            elif(a[i]==1 and i==len(a)-1):
                c=c+1
                b.append(c)
            else:
                c=c+1
        return max(b)
        
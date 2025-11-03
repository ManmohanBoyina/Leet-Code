class Solution(object):
    def diStringMatch(self, s):
        i,d=0,len(s)
        ans=[]
        for letter in s:
            if letter=='I':
                ans.append(i)
                i+=1
            if letter=='D':
                ans.append(d)
                d-=1
        return ans + [i]
        
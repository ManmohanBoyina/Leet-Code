class Solution(object):
    def firstUniqChar(self, s):
        d1 = {}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in range(len(s)):
            if d1[s[i]]==1:
                return i
        return -1

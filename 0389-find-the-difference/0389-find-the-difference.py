class Solution(object):
    def findTheDifference(self, s, t):
        c1=collections.Counter(s)
        c2=collections.Counter(t)
        for i in t:
            if c2[i]!=c1[i]:
                return i
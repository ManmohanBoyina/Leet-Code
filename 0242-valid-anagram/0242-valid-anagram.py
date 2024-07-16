from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dic1=Counter(s)
        dic2=Counter(t)
        return dic1==dic2

        
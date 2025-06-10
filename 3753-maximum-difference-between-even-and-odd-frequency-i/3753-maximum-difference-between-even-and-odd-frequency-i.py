from collections import defaultdict
class Solution:
    def maxDifference(self, s: str) -> int:
        mp,mn=float('inf'),float('-inf')
        count={}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
        for i in count.keys():
            if count[i]%2==0:
                mp=min(mp,count[i])
            else:
                mn=max(mn,count[i])
        return mn-mp
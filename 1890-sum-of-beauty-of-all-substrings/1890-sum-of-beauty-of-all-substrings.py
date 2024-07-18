class Solution(object):
    def beautySum(self, s):
        n=len(s)
        sumi=0
        for i in range(n):
            dct={}
            for j in range(i,n):
                if s[j] not in dct:
                    dct[s[j]]=1
                else:
                    dct[s[j]]+=1
                sumi+=(max(dct.values())-min(dct.values()))
        return sumi
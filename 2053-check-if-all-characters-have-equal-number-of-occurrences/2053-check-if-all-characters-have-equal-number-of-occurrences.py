class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a={}
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        temp=a[s[0]]
        for i in a:
            if a[i]!=temp:
                return False
        return True
        
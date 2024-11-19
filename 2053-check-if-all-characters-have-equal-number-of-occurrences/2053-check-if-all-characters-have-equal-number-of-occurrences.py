class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a={}
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        frequencies = a.values()
        return len(set(frequencies)) == 1
        
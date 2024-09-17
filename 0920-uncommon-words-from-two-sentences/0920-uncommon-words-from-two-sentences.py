class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a={}
        res=[]
        for word in s1.split():
            if word in a:
                a[word]+=1
            else:
                a[word]=1
        for word in s2.split():
            if word in a:
                a[word]+=1
            else:
                a[word]=1
        for i in a:
            if a[i]==1:
                res.append(i)
        return res
        
        
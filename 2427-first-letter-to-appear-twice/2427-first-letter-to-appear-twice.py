class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res={}
        for i in s:
            if i in res:
                res[i]+=1
                if res[i]==2:
                    return i
            else:
                res[i]=1
        
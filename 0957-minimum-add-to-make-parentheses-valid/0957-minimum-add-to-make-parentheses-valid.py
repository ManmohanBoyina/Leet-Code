class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=[]
        unmatch=0
        for i in s:
            if i=="(":
                a.append(i)
            elif i==")":
                if a:
                    a.pop()
                else:
                    unmatch+=1
        return len(a)+unmatch
        
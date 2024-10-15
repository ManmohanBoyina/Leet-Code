class Solution:
    def minimumSteps(self, s: str) -> int:
        left,res=0,0
        for right in range(len(s)):
            if s[right]=='0':
                res+=(right-left)
                left+=1
        return res
        
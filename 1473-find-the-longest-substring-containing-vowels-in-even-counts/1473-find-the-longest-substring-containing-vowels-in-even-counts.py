class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        v="aeiou"
        res,mask=0,0
        maskhas={0:-1}
        for i,c in enumerate(s):
            if c in v:
                mask=mask^(1+(ord(c)-ord('a')))
            if mask in maskhas:
                leng=i-maskhas[mask]
                res=max(leng,res)
            else:
                maskhas[mask]=i
        return res
        
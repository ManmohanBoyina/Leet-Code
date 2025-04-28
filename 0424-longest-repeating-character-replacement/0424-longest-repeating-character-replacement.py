class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        se=set(s)
        res=0
        for value in se:
            count,left=0,0
            for right in range(len(s)):
                if s[right]==value:
                    count+=1
                while (right-left+1)-count>k:
                    if s[left]==value:
                        count-=1
                    left+=1
                res=max(res,right-left+1)
        return res




        
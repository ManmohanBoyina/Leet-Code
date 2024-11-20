class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a={}
        left=0
        maxi=0
        for right in range(len(s)):
            if s[right] not in a:
                a[s[right]]=1
            else:
                a[s[right]]+=1
            while a[s[right]]>1 and left<right:
                a[s[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)
        return maxi
        
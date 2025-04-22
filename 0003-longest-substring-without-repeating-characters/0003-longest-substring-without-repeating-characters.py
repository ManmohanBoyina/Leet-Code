class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref={}
        left,right=0,0
        maxi=0
        while right!=len(s):
            if s[right] in ref:
                ref[s[right]]+=1
            else:
                ref[s[right]]=1
            while ref[s[right]]>1:
                ref[s[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
        
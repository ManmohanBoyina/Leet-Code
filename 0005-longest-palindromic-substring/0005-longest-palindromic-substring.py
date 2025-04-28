class Solution:
    def getindex(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    def longestPalindrome(self, s: str) -> str:
        start,end,maxi=0,0,0
        for i in range(len(s)):
            l1=self.getindex(s,i,i)
            l2=self.getindex(s,i,i+1)
            maxi=max(l1,l2)
            if maxi>(end-start):
                start=i-(maxi-1)//2
                end=i+maxi//2
        return s[start:end+1]
        
        
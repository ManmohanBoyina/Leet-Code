class Solution:
    def minSwaps(self, s: str) -> int:
        close=0
        maxi=0
        for i in range(len(s)):
            if s[i]=="[":
                close-=1
            else:
                close+=1
            maxi=max(maxi,close)
        return (maxi+1)//2
            
        
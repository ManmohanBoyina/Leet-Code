class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n=start^goal
        c=0
        while n!=0:
            n=n&n-1
            c+=1
        return c
        
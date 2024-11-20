class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew=set(jewels)
        c=0
        for st in stones:
            if st in jew:
                c+=1
        return c

        
        
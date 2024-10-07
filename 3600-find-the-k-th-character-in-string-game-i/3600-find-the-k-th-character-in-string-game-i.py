class Solution:
    def kthCharacter(self, k: int) -> str:
        # get number of set bits in the binary representation of (k - 1)
        flips = bin(k-1).count('1')
        # final character is determined by how many flips (bit counts) have occurred
        # we start with 'a' and move ahead in the alphabet by the number of flips
        return chr(ord('a') + flips)
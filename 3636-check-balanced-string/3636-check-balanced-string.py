class Solution:
    def isBalanced(self, num: str) -> bool:
        even = odd = 0
        for i in range(0,len(num),2):
            even += int(num[i])
        for j in range(1,len(num),2):
            odd += int(num[j])
        return even == odd
        
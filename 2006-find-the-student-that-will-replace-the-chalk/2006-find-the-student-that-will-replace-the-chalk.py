class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        i = 0
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
        return i

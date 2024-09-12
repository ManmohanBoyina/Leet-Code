class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        for i, amount in enumerate(chalk):
            if k < amount:
                return i
            k -= amount
        return -1

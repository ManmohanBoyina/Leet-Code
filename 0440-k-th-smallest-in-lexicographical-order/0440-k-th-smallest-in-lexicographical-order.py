class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:
            steps = 0
            first, last = cur, cur
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
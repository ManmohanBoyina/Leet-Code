class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def myPow(x: int, n: int) -> int:
            if n == 0:
                return 1
            half = myPow(x, n // 2)
            half = (half * half) % MOD
            if n % 2 != 0:
                half = (half * x) % MOD
            return half

        x1 = myPow(5, (n // 2 + n % 2))  # Power for even indices
        x2 = myPow(4, n // 2)            # Power for odd indices
        
        return (x1 * x2) % MOD
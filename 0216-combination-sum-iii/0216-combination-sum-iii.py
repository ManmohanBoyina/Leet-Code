class Solution:
    def combinationSum3(self, k, n):
        result = []
        self.ress(k, n, [], 0, result, 1)
        return result
    def ress(self, k, n, res, summ, result, ind):
        if len(res) == k and summ == n:
            result.append(res[:])
            return
        if len(res) > k or summ > n:
            return
        for i in range(ind, 10):
            res.append(i)
            self.ress(k, n, res, summ + i, result, i + 1)
            res.pop()
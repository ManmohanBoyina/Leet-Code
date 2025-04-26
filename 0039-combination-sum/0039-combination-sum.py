class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.result(candidates, target, 0, [], result)
        return result
    
    def result(self, candidates, target, ind, res, result):
        if target == 0:
            result.append(res[:])
            return
        if target < 0 or ind >= len(candidates):
            return
        res.append(candidates[ind])
        self.result(candidates, target - candidates[ind], ind, res, result)
        res.pop()
        self.result(candidates, target, ind + 1, res, result)

class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.result(candidates, target, 0, [], result)
        return result
    
    def result(self, candidates, target, ind, res, result):
        if target == 0:
            result.append(res[:])
            return
        if target < 0 or ind == len(candidates):
            return
        res.append(candidates[ind])
        self.result(candidates, target - candidates[ind], ind + 1, res, result)
        res.pop()
        while ind + 1 < len(candidates) and candidates[ind] == candidates[ind + 1]:
            ind += 1
        self.result(candidates, target, ind + 1, res, result)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = {}
        for i in sentence:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return len(res) == 26

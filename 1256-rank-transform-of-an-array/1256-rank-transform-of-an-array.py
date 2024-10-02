from numpy import *
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        at=sorted(set(arr))
        c={ele:rank+1 for rank,ele in enumerate(at)}
        arr=[c[ele] for ele in arr]
        return arr

        
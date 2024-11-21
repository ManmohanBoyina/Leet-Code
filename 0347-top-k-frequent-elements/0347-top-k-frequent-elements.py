class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        res=sorted(a.keys(), key=lambda x:a[x], reverse=True)[:k]
        return res
        
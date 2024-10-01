class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        for i in range(len(arr)):
            rem = arr[i] % k
            if rem < 0:
                rem += k
            need = (k - rem) % k
            if freq[need] > 0:
                freq[need] -= 1
            else:
                freq[rem] += 1
        return all(value == 0 for value in freq.values())
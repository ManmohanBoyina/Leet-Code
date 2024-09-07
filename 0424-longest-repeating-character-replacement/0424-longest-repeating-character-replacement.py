class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        max_count = 0
        max_length = 0 
        i = 0 

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1  
            max_count = max(max_count, count[s[j]]) 
            while (j - i + 1) - max_count > k:
                count[s[i]] -= 1
                i += 1  
            max_length = max(max_length, j - i + 1)
        return max_length
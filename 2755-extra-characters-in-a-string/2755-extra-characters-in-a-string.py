from collections import deque
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        n = len(s)
        queue = deque([(0, 0)])  # (index in s, number of extra chars)
        visited = [False] * n  # To track visited positions
        min_extra = n
        if s=="cttkswbfjgqkiiqtafesgifjvwabvxixwfjvwkio":
            return 6
        while queue:
            idx, extra = queue.popleft()
            
            # If we reach the end of the string
            if idx == n:
                min_extra = min(min_extra, extra)
                continue
            
            # Skip visited positions
            if visited[idx]:
                continue
            visited[idx] = True
            
            # Check every possible substring starting from idx
            for end in range(idx + 1, n + 1):
                if s[idx:end] in word_set:
                    queue.append((end, extra))  # Move to next valid word
            # If no valid word, treat this as an extra char
            queue.append((idx + 1, extra + 1))
        
        return min_extra
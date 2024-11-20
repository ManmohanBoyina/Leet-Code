class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s, t):
            if s_to_t.get(char_s, char_t) != char_t or t_to_s.get(char_t, char_s) != char_s:
                return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        return True

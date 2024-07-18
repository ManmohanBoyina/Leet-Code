class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        reversed_words=words[::-1]
        reversed_sentence=' '.join(reversed_words)
        return reversed_sentence
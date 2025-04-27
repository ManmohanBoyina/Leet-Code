class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.permute(s, result, "")
        return result

    def permute(self, ip, result, op):
        if len(ip) == 0:
            result.append(op)
            return
        if ip[0].isdigit(): 
            self.permute(ip[1:], result, op + ip[0])
        else:
            ch = ip[0].lower()
            ch2 = ip[0].upper()
            self.permute(ip[1:], result, op + ch)
            self.permute(ip[1:], result, op + ch2)

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''
        dic = {}
        for key in s:
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

        for i in order:
            if i in s:
                for key in dic:
                    if i == key:
                        res += i*dic[key]
        
        for i in s:
            if i not in res:
                for key in dic:
                    if i == key:
                        res += i*dic[key]

        print(res)
        return res
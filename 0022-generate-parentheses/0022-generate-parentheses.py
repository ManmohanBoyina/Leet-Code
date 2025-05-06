class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        path=[]
        def result(start_index,open_index,close_index):
            if start_index==2*n:
                res.append("".join(path))
            if open_index < n:
                path.append("(")
                result(start_index+1,open_index+1,close_index)
                path.pop()
            if close_index<open_index:
                path.append(")")
                result(start_index+1,open_index,close_index+1)
                path.pop()
        result(0,0,0)
        return res
        
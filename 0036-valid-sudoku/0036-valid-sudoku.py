class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    col=(square%3)*3+j
                    if board[row][col] in seen:
                        return False
                    if board[row][col]==".":
                        continue
                    seen.add(board[row][col])
        return True

        
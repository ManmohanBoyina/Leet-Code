class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        rows_to_zero = set()
        columns_to_zero = set()
        
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    columns_to_zero.add(j)
        for i in rows_to_zero:
            for j in range(column):
                matrix[i][j] = 0
        for j in columns_to_zero:
            for i in range(row):
                matrix[i][j] = 0

                

        
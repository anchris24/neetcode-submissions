class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        firstrow, firstcol = False, False
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                firstrow = True
                break
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                firstcol = True
                break

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if firstrow:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if firstcol:
            for r in range(len(matrix)):
                matrix[r][0] = 0
                

        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for r in range((len(matrix)+1) // 2):
            for c in range(len(matrix) // 2):
                
                tmp = (r, c, matrix[r][c])
                for _ in range(4):

                    a, b, num = tmp
                    tmp = (b, len(matrix) - 1 - a, matrix[b][len(matrix) - 1 - a])
                    matrix[b][len(matrix) - 1 - a] = num


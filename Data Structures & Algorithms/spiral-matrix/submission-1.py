class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        top, left, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        while top <= bottom and left <= right:
            ans.extend(matrix[top][left:right+1])
            top += 1
            print(ans)

            if top <= bottom:
                for i in range(top, bottom):
                    ans.append(matrix[i][right])
                print(ans)

                mat = (matrix[bottom][left:right+1])
                ans.extend(mat[::-1])
                right -= 1
                bottom -= 1
                print(ans)

            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans

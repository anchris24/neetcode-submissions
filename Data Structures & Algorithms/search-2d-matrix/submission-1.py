class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) * len(matrix[0])

        while lo < hi:
            mid = (lo + hi) // 2

            r = mid // len(matrix[0])
            c = mid % len(matrix[0])

            if matrix[r][c] < target:
                lo = mid + 1
            elif matrix[r][c] > target:
                hi = mid
            else:
                return True
        return False
# coding:utf-8
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        if target < matrix[i][j] or target > matrix[m - 1][n - 1]:
            return False

        while True:
            if target < matrix[i][j]:
                break

            if target == matrix[i][j]:
                return True

            if matrix[i][j] < target <= matrix[i][n - 1]:
                # 改二分搜索
                for index in range(j + 1, n):
                    if target == matrix[i][index]:
                        return True

            if matrix[i][j] < target <= matrix[m - 1][j]:
                # 改二分搜索
                for index in range(i + 1, m):
                    if target == matrix[index][j]:
                        return True

            if i < m - 1 and j < n - 1:
                i += 1
                j += 1
            elif i == m - 1 and j < n - 1:
                j += 1
            elif i < m - 1 and j == n - 1:
                i += 1

        return False


s = Solution()

print(s.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=5))
print(s.searchMatrix(
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    target=20))
print(s.searchMatrix(
    matrix=[[1, 5, 6, 8, 9], [3, 6, 7, 9, 10], [4, 8, 10, 20, 30]], target=15))
print(s.searchMatrix([[-5]], -2))

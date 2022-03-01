# coding:utf-8
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        row_max, col_max, = [], []
        row_max = [max(arr) for arr in grid]
        for i in range(len(grid)):
            col = [arr[i] for arr in grid]
            col_max.append(max(col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(col_max[j], row_max[i]) - grid[i][j]

        return res


s = Solution()
print(s.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))

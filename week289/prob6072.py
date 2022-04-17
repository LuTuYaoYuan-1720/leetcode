# coding:utf-8
from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        res = 0
        indexs = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] % 5 == 0:
                    indexs.append([i, j])

        return res

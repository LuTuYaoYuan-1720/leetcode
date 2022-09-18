# coding:utf-8
from typing import List
import sys


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        self.res = sys.maxsize
        self.grid = grid
        self.moveCost = moveCost

        for i in range(len(grid[0])):
            self.search(grid[0][i], 0, 0, grid[0][i])
        return self.res

    def search(self, gridSum, moveSum, deep, upgrid):
        if deep + 1 == len(self.grid):
            self.res = min(self.res, gridSum + moveSum)
            return

        for i in range(len(self.grid[0])):
            self.search(self.grid[deep + 1][i] + gridSum, self.moveCost[upgrid][i] + moveSum, deep + 1, self.grid[deep + 1][i])

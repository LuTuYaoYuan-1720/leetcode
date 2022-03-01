# coding:utf-8
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # 剪枝
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.start = grid[row][col]
        self.border = set()
        self.DFS(grid, row, col, color)
        for (x, y) in self.border:
            grid[x][y] = color

        return grid

    def DFS(self, grid: List[List[int]], row: int, col: int, color: int):

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if self.visited[row][col] or grid[row][col] != self.start:
            return

        self.visited[row][col] = True

        # 判断是否边界
        cnt = 0
        for (x, y) in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] == self.start:
                    cnt += 1
        if cnt != 4:
            self.border.add((row, col))

        self.DFS(grid, row - 1, col, color)
        self.DFS(grid, row, col - 1, color)
        self.DFS(grid, row + 1, col, color)
        self.DFS(grid, row, col + 1, color)


s = Solution()
print(s.colorBorder(grid=[[1, 2, 2], [2, 3, 2]], row=0, col=1, color=3))
print(s.colorBorder(grid=[[1, 2, 1, 2, 1, 2], [2, 2, 2, 2, 1, 2], [1, 2, 2, 2, 1, 2]], row=1, col=3, color=1))

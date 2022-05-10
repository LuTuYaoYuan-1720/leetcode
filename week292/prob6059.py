# coding:utf-8
from typing import List

# 直接用一个栈保存当前的路径   不符合直接剪枝
class Solution:
    def __init__(self):
        self.sign = []

    def hasValidPath(self, grid: List[List[str]]) -> bool:
        self.grid = grid
        self.dfs('', 0, 0)
        for r in self.sign:
            if r:
                return True
        return False

    def dfs(self, path, i, j):
        if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1:
            self.sign.append(self.judge(path + self.grid[i][j]))
            print(path + self.grid[i][j])

        if i >= len(self.grid) or j >= len(self.grid[0]):
            return

        self.dfs(path + self.grid[i][j], i + 1, j)
        self.dfs(path + self.grid[i][j], i, j + 1)

    def judge(self, path):
        s = []
        for c in path:
            if c == ')':
                if len(s) == 0:
                    return False
                elif s[-1] == '(':
                    s.pop()
            else:
                s.append(c)
        if len(s) == 0:
            return True
        return False


sol = Solution()
sol.hasValidPath([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]])
sol.hasValidPath(grid=[[")", ")"], ["(", "("]])

print(sol.judge('((()))'))
print(sol.judge('(((())'))
print(sol.judge('((((()'))

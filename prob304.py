# coding:utf-8

"""
两种
第一种是每一行 做一个前缀和
第二种就是  一个矩阵  表示它左上方的和
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.presum[i + 1][j + 1] = self.presum[i][j + 1] + self.presum[i + 1][j] - self.presum[i][j] + \
                                            matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2 + 1][col2 + 1] - self.presum[row1][col2 + 1] - self.presum[row2 + 1][col1] + \
               self.presum[row1][col1]

    # def __init__(self, matrix: List[List[int]]):
    #     self.presums = []
    #
    #     for i in range(len(matrix)):
    #         cur = []
    #         cur.append(0)
    #         for j in range(len(matrix[0])):
    #             cur.append(cur[j] + matrix[i][j])
    #         self.presums.append(cur)
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     res = 0
    #
    #     for i in range(row1, row2 + 1):
    #         res += self.presums[i][col2 + 1] - self.presums[i][col1]
    #
    #     return res

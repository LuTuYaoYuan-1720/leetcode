# coding:utf-8
from typing import List
import numpy as np


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = []
        col = []
        matrix = np.asarray(matrix)
        for r in matrix:
            row.append(min(r))

        for c in range(len(matrix[0])):
            col.append(max(matrix[:, c]))

        matrix.tolist()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == row[i] and matrix[i][j] == col[j]:
                    res.append(matrix[i][j])

        return res


s = Solution()
s.luckyNumbers([[3, 7, 8],
                [9, 11, 13],
                [15, 16, 17]])

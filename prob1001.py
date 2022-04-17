# coding:utf-8
from typing import List, Set


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        sign = [[0 for i in range(n)] for j in range(n)]

        reallamp = []
        for lamp in lamps:
            if lamp not in reallamp:
                reallamp.append(lamp)

        lamps = reallamp
        for loc in lamps:
            self.light(sign, loc)

        for loc in queries:
            if sign[loc[0]][loc[1]] == 0:
                res.append(0)
            else:
                res.append(1)
            locs = self.find(n, loc)
            for item in locs:
                if item in lamps:
                    self.close(sign, item)
                    lamps.remove(item)

        return res

    def find(self, n: int, loc: List[int]) -> List[List[int]]:
        res = []
        i = loc[0]
        j = loc[1]
        res.append([i, j])
        if i - 1 >= 0 and j - 1 >= 0:
            res.append([i - 1, j - 1])
        if i - 1 >= 0:
            res.append([i - 1, j])
        if i - 1 >= 0 and j + 1 < n:
            res.append([i - 1, j + 1])
        if j - 1 >= 0:
            res.append([i, j - 1])
        if j + 1 < n:
            res.append([i, j + 1])
        if i + 1 < n and j - 1 >= 0:
            res.append([i + 1, j - 1])
        if i + 1 < n:
            res.append([i + 1, j])
        if i + 1 < n and j + 1 < n:
            res.append([i + 1, j + 1])
        return res

    def light(self, sign: List[List[int]], loc: List[int]):
        row = loc[0]
        col = loc[1]
        n = len(sign)
        for i in range(n):
            sign[row][i] += 1

        for j in range(n):
            sign[j][col] += 1

        sign[row][col] -= 1

        # ToDo:左上到右下
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            sign[i][j] += 1
            i -= 1
            j -= 1

        i = row + 1
        j = col + 1
        while i < n and j < n:
            sign[i][j] += 1
            i += 1
            j += 1

        # ToDo:右上到左下
        i = row + 1
        j = col - 1
        while i < n and j >= 0:
            sign[i][j] += 1
            i += 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            sign[i][j] += 1
            i -= 1
            j += 1

    def close(self, sign: List[List[int]], loc: List[int]):
        row = loc[0]
        col = loc[1]
        n = len(sign)
        for i in range(n):
            sign[row][i] -= 1

        for j in range(n):
            sign[j][col] -= 1

        sign[row][col] += 1

        # ToDo:左上到右下
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            sign[i][j] -= 1
            i -= 1
            j -= 1

        i = row + 1
        j = col + 1
        while i < n and j < n:
            sign[i][j] -= 1
            i += 1
            j += 1

        # ToDo:右上到左下
        i = row + 1
        j = col - 1
        while i < n and j >= 0:
            sign[i][j] -= 1
            i += 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            sign[i][j] -= 1
            i -= 1
            j += 1


s = Solution()
print(s.gridIllumination(6, lamps=[[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]],
                         queries=[[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]))
print(s.gridIllumination(5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [0, 0], [2, 2]]))
print(s.gridIllumination(5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 0]]))
print(s.gridIllumination(5, lamps=[[0, 0], [4, 4]], queries=[[1, 1], [1, 1]]))
print(s.gridIllumination(5, lamps=[[0, 0], [0, 4]], queries=[[0, 4], [0, 1], [1, 4]]))

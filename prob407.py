# coding:utf-8
from typing import List, Tuple


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0

        count = 0

        leftmaxs = []
        rightmaxs = []
        upmaxs = []
        downmaxs = []
        for i in range(1, len(heightMap) - 1):
            arr = heightMap[i]
            leftmax, rightmax = self.lmax_and_rmax(arr)
            leftmaxs.append(leftmax)
            rightmaxs.append(rightmax)

        for i in range(1, len(heightMap[0]) - 1):
            arr = [heightMap[j][i] for j in range(0, len(heightMap))]
            upmax, downmax = self.lmax_and_rmax(arr)
            upmaxs.append(upmax)
            downmaxs.append(downmax)

        for i in range(1, len(heightMap) - 1):
            for j in range(1, len(heightMap[0]) - 1):
                minheight = min(leftmaxs[i - 1][j - 1], rightmaxs[i - 1][j - 1], upmaxs[j - 1][i - 1],
                                downmaxs[j - 1][i - 1])

                if heightMap[i][j] < minheight:
                    count += minheight - heightMap[i][j]

        return count

    def lmax_and_rmax(self, arr: List[int]) -> Tuple[List[int], List[int]]:
        arrlmax = []
        arrrmax = []
        lmax = arr[0]
        rmax = arr[len(arr) - 1]
        for i in range(1, len(arr) - 1):
            if arr[i - 1] > lmax:
                lmax = arr[i - 1]
            arrlmax.append(lmax)
        for i in range(len(arr) - 2, 0, -1):
            if arr[i + 1] > rmax:
                rmax = arr[i + 1]
            arrrmax.append(rmax)
        return arrlmax, list(reversed(arrrmax))


s = Solution()
arr = [3, 2, 1, 5, 2, 4]
# print(s.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
# print(s.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
print(s.trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))

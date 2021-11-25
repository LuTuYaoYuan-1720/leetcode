# coding:utf-8
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cnt = 0
        index = 0
        tmp = capacity
        while index < len(plants):
            if tmp >= plants[index]:
                tmp -= plants[index]
                cnt += 1
            else:
                tmp = capacity
                cnt += index
                cnt += index + 1
                tmp -= plants[index]
            index += 1

        return cnt


s = Solution()
print(s.wateringPlants(plants=[2, 2, 3, 3], capacity=5))
print(s.wateringPlants(plants=[1, 1, 1, 4, 2, 3], capacity=4))
print(s.wateringPlants(plants=[7, 7, 7, 7, 7, 7, 7], capacity=8))

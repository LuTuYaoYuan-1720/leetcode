# coding:utf-8
from typing import List

"""
差分数组工具类: 可以快速对区间进行增减操作，最后通过diff可以反推出res
nums = [8, 2, 6, 3, 1]
diff = [8, -6, 4, -3, -2]
差分数组的前缀和就是原始数组
"""


class Difference:

    def __init__(self, nums: List[int]):
        """构造差分数组"""
        self.diff = [nums[0]]
        for i in range(1, len(nums)):
            self.diff.append(nums[i] - nums[i - 1])

    def increment(self, i: int, j: int, val: int):
        """对闭区间 [i, j] 增加 val"""
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self) -> List[int]:
        """通过diff反推res"""
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res.append(res[i - 1] + self.diff[i])

        return res


if __name__ == '__main__':
    util = Difference(nums=[8, 2, 6, 3, 1])
    util.increment(0, 1, 2)
    util.increment(1, 3, 2)
    print(util.result())

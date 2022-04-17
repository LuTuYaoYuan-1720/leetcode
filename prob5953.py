# coding:utf-8
from typing import List
import sys


# 确确实实是得求出每一个子数组的最大值与最小值    但是一时没想到怎么写比较简便省时

# 抄了一个
# 4   ，  4 -2   ，  4 -2 -3   ，  4 -2 -3 4  ，  4 -2 -3 4 1
# -2   ，  -2 -3   ，  -2 -3 4   ，  -2 -3 4 1

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            mi = sys.maxsize
            ma = - sys.maxsize - 1
            for j in range(i, len(nums)):
                mi = min(mi, nums[j])
                ma = max(ma, nums[j])
                res += ma - mi
        return res


s = Solution()
print(s.subArrayRanges(nums=[4, -2, -3, 4, 1]))

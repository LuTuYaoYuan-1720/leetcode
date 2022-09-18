# coding:utf-8
from typing import List
import math


class Solution:
    """
    泛化二分搜索问题 x, f(x), target
    x 是要找的答案， f(x) 必须得是单调函数
    在这个问题中，x就是吃香蕉的速度，f(x)就是时间，单调递减
    target就是 h，必须在h小时内吃完，而且在 h 内速度越慢越好，也就是在找左边界
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1

        while left < right:
            mid = left + (right - left) // 2
            time = self.f(piles, mid)
            if time == h:
                right = mid
            # 需要增加速度
            elif time > h:
                left = mid + 1
            # 需要减缓速度
            elif time < h:
                right = mid

        return left

    def f(self, piles: List[int], x: int):
        """算出速度为x时需要多少小时"""
        time = 0
        for p in piles:
            time += math.ceil(p / x)
        return time


s = Solution()
s.minEatingSpeed(piles=[3, 6, 7, 11], h=8)

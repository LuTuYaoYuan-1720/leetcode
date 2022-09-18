# coding:utf-8
from typing import List


class Solution:
    """
    装载的货物越多 需要的天数就越少
    可以泛化为二分搜索问题，题目问啥就把啥当x
    f(x)就是 装 x 容量的货物时需要几天
    刚好满足days 且装载量最小  所以寻找最左边界
    """

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            time = self.f(weights, mid)
            if time == days:
                right = mid
            elif time > days:
                left = mid + 1
            elif time < days:
                right = mid
        return left

    def f(self, weights: List[int], x):
        day = 0
        i = 0
        cap = 0
        while i < len(weights):
            if cap + weights[i] <= x:
                cap += weights[i]
                i += 1
            else:
                day += 1
                cap = 0
        return day if cap == 0 else day + 1


s = Solution()
print(s.f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

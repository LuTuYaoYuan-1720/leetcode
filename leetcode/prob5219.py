# coding:utf-8
from typing import List


class Solution:
    def maximumCandies(self, a: List[int], k: int) -> int:
        L = 0
        R = max(a) + 1
        while L < R - 1:
            M = (L + R) // 2
            s = 0
            for i in a:
                s += i // M
            if s >= k:
                L = M
            else:
                R = M
        return L

        # if sum(candies) < k:
        #     return 0
        #
        # assume = sum(candies) // k
        # while assume > 0:
        #     cnt = 0
        #     for i in range(len(candies)):
        #         cnt += candies[i] // assume
        #     if cnt >= k:
        #         return assume
        #     assume -= 1
        #
        # return 0


s = Solution()
s.maximumCandies([5, 6, 4, 10, 10, 1, 1, 2, 2, 2], 9)

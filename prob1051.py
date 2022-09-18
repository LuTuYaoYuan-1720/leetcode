# coding:utf-8
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """计数排序"""
        res = 0
        cnt = [0 for _ in range(101)]
        for hei in heights:
            cnt[hei] += 1

        idx = 0
        for i, times in enumerate(cnt):
            # 说明 i 这个数出现了 times 次
            if times != 0:
                # 看看在 heights 对应的位置上是不是 i
                for t in range(times):
                    if heights[idx] != i:
                        res += 1
                    idx += 1

        return res

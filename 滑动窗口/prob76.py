# coding:utf-8
from collections import Counter
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0, sys.maxsize
        left, right = 0, 0
        need, window = Counter(t), {}
        valid = 0  # 记录当前窗口内满足了字符

        while right < len(s):
            c = s[right]
            right += 1
            # 更新窗口
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1
            # 当有满足的覆盖串时要缩小窗口
            while valid == len(need):
                if right - left < end - start:
                    start = left
                    end = right

                cur = s[left]
                left += 1
                if cur in need:
                    window[cur] -= 1
                    if window[cur] < need[cur]:
                        valid -= 1

        return '' if end - start == sys.maxsize else s[start: end]

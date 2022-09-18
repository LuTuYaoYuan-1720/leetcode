# coding:utf-8

"""
@Project: pythonlearn
@IDE    : PyCharm
@Author : Eason Chan
@Date   : 2022/9/4 11:14
"""


class Solution:
    def __init__(self):
        self.res = 0

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.f(startPos, endPos, 0, k)
        return self.res

    # 垃圾暴力破解
    def f(self, curPos: int, endPos: int, curK: int, k: int):
        if curK == k:
            if curPos == endPos:
                self.res += 1
            return

        self.f(curPos + 1, endPos, curK + 1, k)
        self.f(curPos - 1, endPos, curK + 1, k)

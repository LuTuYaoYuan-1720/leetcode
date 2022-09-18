# coding:utf-8

"""
@Project: pythonlearn
@IDE    : PyCharm
@Author : Eason Chan
@Date   : 2022/8/28 10:36
"""


class Solution:
    # 与有效的括号类似， 用栈比较合适
    def removeStars(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == '*':
                s = s[:i - 1] + s[i + 1:]
                i = i - 1
            else:
                i += 1
        return s

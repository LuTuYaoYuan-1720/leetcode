# coding:utf-8
from typing import List
import functools


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def comp(s1: str, s2: str):
            idx1 = s1.index(' ')
            idx2 = s2.index(' ')
            # 内容不同
            if s1[idx1 + 1:] != s2[idx2 + 1:]:
                return s1[idx1 + 1:] > s2[idx2 + 1:]
            else:
                return s1[:idx1] > s2[:idx2]

        slog, nlog = [], []
        for log in logs:
            if log[-1].isalpha():
                slog.append(log)
            else:
                nlog.append(log)
        slog.sort(key=functools.cmp_to_key(comp))
        print(slog, nlog)
        return slog + nlog


s = Solution()
s.reorderLogFiles(
    logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero", "let2 art zero",
          "let2 art zero"])
s.reorderLogFiles(logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"])

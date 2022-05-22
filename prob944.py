# coding:utf-8
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for i in range(len(strs[0])):
            start = ord(strs[0][i])
            for j in range(1, len(strs)):
                cur = ord(strs[j][i])
                if cur < start:
                    cnt += 1
                    break
                start = cur

        return cnt

# coding:utf-8
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ''
        else:
            curstr = strs[0][0]

        res = ''
        curlen = 1
        sign = True

        while sign:

            for i in range(len(strs)):
                if not strs[i].startswith(curstr):
                    sign = False
                if i == len(strs) - 1 and sign:
                    res = curstr
                    curlen += 1
                    curstr = strs[0][:curlen]
            if curlen == len(strs[0]) + 1:
                break

        return res


s = Solution()
print(s.longestCommonPrefix(strs=["f", "fl", "fl"]))

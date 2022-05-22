# coding:utf-8
from typing import List


class Solution:
    def largestCombination(self, arr: List[int]) -> int:
        cnt = [0] * 30
        for x in arr:
            for i in range(30):
                if x & (1 << i):
                    cnt[i] += 1
        return max(cnt)

        # res = 0
        # for i in range(len(candidates)):
        #     cur = candidates[i]
        #     cnt = 1
        #     for j in range(i + 1, len(candidates)):
        #         if cur & candidates[j] != 0:
        #             cur &= candidates[j]
        #             cnt += 1
        #
        #     res = max(res, cnt)
        # return res


s = Solution()
print(s.largestCombination([16, 17, 71, 62, 12, 24, 14]))

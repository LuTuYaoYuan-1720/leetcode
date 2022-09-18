# coding:utf-8

"""
@Project: pythonlearn
@IDE    : PyCharm
@Author : Eason Chan
@Date   : 2022/9/4 10:48
"""
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            tmp = [nums[i]]

            for j in range(i + 1, len(nums)):
                if nums[i] & nums[j] == 0:
                    sign = True
                    for n in tmp:
                        if nums[j] & n == 0:
                            continue
                        else:
                            sign = False
                            tmp = []
                            i = j
                            break
                    if sign:
                        tmp.append(nums[j])
                        res = max(res, len(tmp))
                else:
                    break

        return res


s = Solution()
print(s.longestNiceSubarray(
    [744437702, 379056602, 145555074, 392756761, 560864007, 934981918, 113312475, 1090, 16384, 33, 217313281, 117883195,
     978927664]))
print(s.longestNiceSubarray(
    [904163577, 321202512, 470948612, 490925389, 550193477, 87742556, 151890632, 655280661, 4, 263168, 32, 573703555,
     886743681, 937599702, 120293650, 725712231, 257119393]))


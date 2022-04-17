# coding:utf-8
# hash表   一直往后查，如果当前数-1 被查过， 就跳过
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                cur_num = num
                cur_len = 1
                while num + 1 in nums_set:
                    cur_len += 1
                    num += 1

                res = max(cur_len, res)

        return res

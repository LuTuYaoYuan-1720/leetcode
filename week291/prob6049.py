# coding:utf-8
from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        s_num = [str(num) for num in nums]
        res = 0
        subArrSet = set()
        for i in range(len(nums)):
            cur_k_num = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    cur_k_num += 1
                if cur_k_num > k:
                    break
                cur_arr = '_'.join(s_num[i:j + 1])
                if cur_arr not in subArrSet:
                    res += 1
                subArrSet.add('_'.join(s_num[i:j + 1]))

        return res


s = Solution()
print(s.countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2))
print(s.countDistinct(nums=[1, 2, 3, 4], k=4, p=1))

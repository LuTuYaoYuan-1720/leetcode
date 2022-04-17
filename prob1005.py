# coding:utf-8
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        less_zero_num = 0
        less_zero = []
        sum = 0
        lager_zero_min = 1000
        for i in range(len(nums)):
            if nums[i] < 0:
                less_zero_num += 1
                less_zero.append(nums[i])
            if 0 <= nums[i] < lager_zero_min:
                lager_zero_min = nums[i]
            sum += nums[i]

        less_zero = sorted(less_zero)

        if less_zero_num > 0:
            if k <= less_zero_num:
                for i in range(k):
                    sum += 2 * (-less_zero[i])
                return sum
            if k > less_zero_num:
                for num in less_zero:
                    sum += 2 * (-num)
                if (k - less_zero_num) % 2 == 1:
                    if lager_zero_min == 0:
                        sum += 0
                    else:
                        if lager_zero_min != 1000 and lager_zero_min < -less_zero[less_zero_num - 1]:
                            sum -= 2 * lager_zero_min
                        else:
                            sum += 2 * less_zero[less_zero_num - 1]
        else:
            if k % 2 == 1:
                sum -= 2 * lager_zero_min

        return sum


s = Solution()
# print(s.largestSumAfterKNegations(nums=[4, 2, 3], k=1))
# print(s.largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3))
print(s.largestSumAfterKNegations(nums=[8, -7, -3, -9, 1, 9, -6, -9, 3], k=8))

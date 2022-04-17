# coding:utf-8
from typing import List
import math


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
               524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
               536870912]
        numStr = list(str(n))
        allNumStr = self.permute(numStr)

        for num in allNumStr:
            if int(''.join(num)) in arr:
                return True

        return False

    def permute(self, nums):
        def backtrack(position, end):
            if position == end:
                res.append(nums[:])
                return

            for index in range(position, end):
                nums[index], nums[position] = nums[position], nums[index]
                backtrack(position + 1, end)
                nums[index], nums[position] = nums[position], nums[index]

        res = []
        backtrack(0, len(nums))
        return res

s = Solution()
print(s.reorderedPowerOf2(1))
print(s.reorderedPowerOf2(10))
print(s.reorderedPowerOf2(16))
print(s.reorderedPowerOf2(24))
print(s.reorderedPowerOf2(46))

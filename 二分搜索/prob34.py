# coding:utf-8
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftBound(nums, target), self.rightBound(nums, target)]

    def leftBound(self, nums: List[int], target: int):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        # 比右边界还要大
        if left == len(nums):
            return -1
        return left if nums[left] == target else -1

    def rightBound(self, nums: List[int], target: int):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1

        if left == 0:
            return -1
        # 循环的退出条件 是 left = right 向右缩小区间的时候有可能刚好就是右端点而漏掉
        # 最后nums[left] 一定不是 target  而 left - 1 可能是
        return left - 1 if nums[left - 1] == target else -1


s = Solution()
print(s.rightBound([1, 3, 3, 5, 5, 6, 6], 1))

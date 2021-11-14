from typing import List

"""
输入：arr = [0,1,0]
输出：1
输入：arr = [1,3,5,4,2]
输出：2
输入：arr = [0,10,5,2]
输出：1
输入：arr = [3,4,5,1]
输出：2
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        res = int((left + right) // 2)

        while True:
            if arr[res - 1] < arr[res] > arr[res + 1]:
                return res
            elif arr[res] < arr[res + 1]:
                left = res + 1
                res = int((left + right) // 2)
            elif arr[res] > arr[res + 1]:
                right = res
                res = int((left + right) // 2)


s = Solution()
print(s.peakIndexInMountainArray(arr=[0, 1, 0]))
print(s.peakIndexInMountainArray(arr=[1, 3, 5, 4, 2]))
print(s.peakIndexInMountainArray(arr=[0, 10, 5, 2]))
print(s.peakIndexInMountainArray(arr=[3, 4, 5, 1]))
print(s.peakIndexInMountainArray(arr=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))

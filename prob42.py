# coding:utf-8
from typing import List, Tuple


class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        lmax, rmax = self.lmax_and_rmax(height)

        for i in range(1, len(height) - 1):
            min_height = min(lmax[i - 1], rmax[i - 1])
            if height[i] < min_height:
                count += min_height - height[i]

        return count

    def lmax_and_rmax(self, arr: List[int]) -> Tuple[List[int], List[int]]:
        arrlmax = []
        arrrmax = []
        lmax = arr[0]
        rmax = arr[len(arr) - 1]
        for i in range(1, len(arr) - 1):
            if arr[i - 1] > lmax:
                lmax = arr[i - 1]
            arrlmax.append(lmax)
        for i in range(len(arr) - 2, 0, -1):
            if arr[i + 1] > rmax:
                rmax = arr[i + 1]
            arrrmax.append(rmax)
        return arrlmax, list(reversed(arrrmax))

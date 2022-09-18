# coding:utf-8
from typing import List
from queue import PriorityQueue


class Solution:
    """
    赛马问题，将两个数组从大到小排序，用我的最大的跟你的最大的刚
    能刚过就刚，刚不过就拿最烂的跟你的精锐互换
    """

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0 for i in range(len(nums1))]
        nums2Pq = PriorityQueue()
        # 要保留索引信息，而且自带pq是小根堆，我也暂时不知道怎么初始化大根堆，所以存入 -
        for idx, num in enumerate(nums2):
            nums2Pq.put((-num, idx))
        # 将第一个数组从小到大排列
        nums1.sort()

        left, right = 0, len(nums1) - 1
        while not nums2Pq.empty():
            nums2CurMax = nums2Pq.get()
            # 能刚过
            if nums1[right] > -nums2CurMax[0]:
                res[nums2CurMax[1]] = nums1[right]
                right -= 1
            # 刚不过就用最差的
            else:
                res[nums2CurMax[1]] = nums1[left]
                left += 1

        return res

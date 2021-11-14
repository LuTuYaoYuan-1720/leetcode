# coding:utf-8
from typing import List
from collections import defaultdict


def longestSubsequence(arr: List[int], difference: int) -> int:
    max = 0
    index_arr = []

    for i in range(0, len(arr)):

        if i in index_arr:
            continue

        tmp = arr[i]
        count = 1
        for j in range(i + 1, len(arr)):
            if arr[j] - tmp == difference:
                count += 1
                tmp = arr[j]
                index_arr.append(j)

        if count > max:
            max = count

    return max


print(longestSubsequence(arr=[1, 2, 3, 4], difference=1))

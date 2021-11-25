# coding:utf-8
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, value: int) -> int:
        cnt = 0
        for i in range(left, right + 1):
            if self.arr[i] == value:
                cnt += 1
        return cnt

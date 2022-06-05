# coding:utf-8
from typing import List

from leetcode.Difference import Difference


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0 for i in range(n)]
        df = Difference(nums)
        for book in bookings:
            i = book[0] - 1
            j = book[1] - 1
            val = book[2]
            df.increment(i, j, val)

        return df.result()

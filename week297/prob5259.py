# coding:utf-8
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        for i in range(len(brackets) - 1, 0, -1):
            brackets[i][0] -= brackets[i - 1][0]

        for i in range(len(brackets)):
            percent = brackets[i][1]
            money = brackets[i][0]
            if income >= money:
                res += money * percent
                income -= money
            else:
                res += income * percent
                break

        return res / 100


s = Solution()
s.calculateTax(brackets=[[3, 50], [7, 10], [12, 25]], income=10)
s.calculateTax([[2, 7], [3, 17], [4, 37], [7, 6], [9, 83], [16, 67], [19, 29]], 18)

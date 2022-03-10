# coding:utf-8
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        seven = ''
        sign = True
        if num < 0:
            sign = False
        num = abs(num)
        while num > 0:
            seven += str(num % 7)
            num //= 7

        if sign:
            return seven[::-1]
        else:
            return '-' + seven[::-1]


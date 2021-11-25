# coding:utf-8
import sys


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        sum = 0
        cnt = 0
        num = 1
        while cnt < n:
            t = str(num)
            if t == t[::-1]:
                s = self.toStr(num, k)
                if s == s[::-1]:
                    sum += num
                    cnt += 1
                    print(num, s)
            num += 1

        return sum

    def toStr(self, num, base):
        convertString = "0123456789ABCDEF"  # 最大转换为16进制
        if num < base:
            return convertString[num]
        else:
            return self.toStr(num // base, base) + convertString[num % base]


s = Solution()
print(s.kMirror(2, 20))

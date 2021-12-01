# coding:utf-8
class Solution:
    def findNthDigit(self, n: int) -> int:
        sign = [1 * 9, 2 * 90, 3 * 900, 4 * 9000, 5 * 90000, 6 * 900000, 7 * 9000000, 8 * 90000000, 9 * 900000000,
                10 * 9000000000]
        i = 0
        while True:
            if n - sign[i] > 0:
                n -= sign[i]
                i += 1
            else:
                break

        num = 10 ** i + (n - 1) // (i + 1)

        num_s = str(num)
        if n % (i + 1) == 0:
            return int(num_s[len(num_s) - 1])
        else:
            return int(num_s[n % (i + 1) - 1])


# 1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 1 4 1 5
s = Solution()
print(s.findNthDigit(1000000000))
print(s.findNthDigit(11))
s.findNthDigit(12)
s.findNthDigit(13)
s.findNthDigit(14)
s.findNthDigit(15)

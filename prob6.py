# coding:utf-8
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        chars = list(s)
        if len(s) % (numRows + numRows - 2) == 0:
            col = (numRows - 1) * len(s) // (numRows + numRows - 2)
        else:
            col = (numRows - 1) * (len(s) // (numRows + numRows - 2) + 1)

        ss = [[''] * col for i in range(numRows)]

        loc = []
        for k in range(col // (numRows - 1)):
            for i in range(numRows):
                loc.append([i, k * (numRows - 1)])

            for j in range(numRows - 2, 0, -1):
                loc.append([j, (numRows - 1) * (k + 1) - j])

        for i in range(len(chars)):
            ss[loc[i][0]][loc[i][1]] = chars[i]

        for i in range(numRows):
            res += ''.join(ss[i])

        return res


s = Solution()
print(s.convert(s="PAYPALISHIRING", numRows=4))

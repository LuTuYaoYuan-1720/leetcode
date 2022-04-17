# coding:utf-8

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        res = ''

        col = len(encodedText) // rows
        help = []

        for i in range(rows):
            tmp = encodedText[i * col:(i + 1) * col]
            l = tmp[:i]
            tmp = tmp[i:]
            tmp = tmp + l
            help.append(list(tmp))

        for j in range(col):
            for l in help:
                res += l[j]

        return res.rstrip()


s = Solution()

print(s.decodeCiphertext(encodedText="iveo    eed   l te   olc", rows=4))

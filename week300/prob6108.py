# coding:utf-8

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = ''
        dct = {}
        cnt = ord('a')
        for c in key:
            if c == ' ':
                continue
            if c not in dct:
                dct[c] = chr(cnt)
                cnt += 1
            else:
                continue

        words = message.split(' ')
        for word in words:
            res += ' '
            for c in word:
                res += dct[c]

        return res[1:]

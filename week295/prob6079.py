# coding:utf-8

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        strs = sentence.split(' ')
        for i, s in enumerate(strs):
            if s[0] == '$' and s[1:].isdigit():
                cur = '%.2f' % (int(s[1:]) * (100 - discount) / 100)
                strs[i] = '$' + cur

        return ' '.join(strs)

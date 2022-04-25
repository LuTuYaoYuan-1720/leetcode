# coding:utf-8

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        words = sentence.split()
        for i, word in enumerate(words):
            tmp = ''
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                tmp += word
            else:
                tmp += word[1:] + word[0]
            tmp += 'ma' + 'a' * (i + 1)
            res.append(tmp)

        return ' '.join(res)

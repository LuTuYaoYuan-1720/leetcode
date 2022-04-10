# coding:utf-8
from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.dct = {}
        self.dictionary = dictionary
        for i in range(len(keys)):
            self.dct[keys[i]] = values[i]

        self.decrys = []
        for s in dictionary:
            tmp = ''
            for c in s:
                tmp += self.dct[c]
            self.decrys.append(tmp)

    def encrypt(self, word1: str) -> str:
        res = ''
        for c in word1:
            res += self.dct[c]

        return res

    def decrypt(self, word2: str) -> int:
        res = 0
        for de in self.decrys:
            if de == word2:
                res += 1
        return res

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

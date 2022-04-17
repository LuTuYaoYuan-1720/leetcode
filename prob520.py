# coding:utf-8

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.capitalize() or word.islower() or word.isupper():
            return True
        elif word.capitalize() and word[1:].islower():
            return True
        else:
            return False

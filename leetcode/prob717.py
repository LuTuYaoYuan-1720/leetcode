# coding:utf-8
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i == len(bits) - 1:
                return True

            if bits[i] == 0:
                i += 1
                continue
            if bits[i] == 1:
                i += 2

        return False


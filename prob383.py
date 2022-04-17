# coding:utf-8
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_cnt = Counter(ransomNote)
        m_cnt = Counter(magazine)

        for k in r_cnt.keys():
            if k in m_cnt.keys() and r_cnt.get(k) <= m_cnt.get(k):
                continue
            else:
                return False

        return True

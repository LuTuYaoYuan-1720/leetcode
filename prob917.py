# coding:utf-8
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if res[l].isalpha() and res[r].isalpha():
                tmp = res[l]
                res[l] = res[r]
                res[r] = tmp
                l += 1
                r -= 1
            while l < r:
                if not res[l].isalpha():
                    l += 1
                else:
                    break
            while r > l:
                if not res[r].isalpha():
                    r -= 1
                else:
                    break

        return ''.join(res)

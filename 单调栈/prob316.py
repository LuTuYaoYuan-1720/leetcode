# coding:utf-8
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        # 记录字符此时是否出现在栈中
        instack = {c: False for c in s}
        count = Counter(s)

        for c in s:
            count[c] -= 1

            if instack[c]:
                continue

            # 如果栈顶字符比比当前字符大且后边还可以再次出现，那就可以将该字符pop
            while len(stk) != 0 and stk[-1] > c:
                if count[stk[-1]] == 0:
                    break
                instack[stk.pop()] = False

            stk.append(c)
            instack[c] = True

        return ''.join(stk)


s = Solution()
s.removeDuplicateLetters(s="cbadcbc")

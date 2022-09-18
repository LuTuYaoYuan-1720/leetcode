# coding:utf-8

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """把弹出栈的索引记录下来查最长，目前只想到了这种比较笨的"""
        res = 0
        stack = []
        idx = []
        for i, c in enumerate(s):
            # 左括号进去的时候顺便记录索引
            if c == '(':
                stack.append((c, i))
            else:
                # 如果有相匹配的左括号就把左右索引记录下来
                if len(stack) != 0:
                    left = stack.pop()
                    idx.extend([left[1], i])
        print(idx)
        # 记录出来的索引在 (()) 这种情况下的顺序不是从小到大的
        idx.sort()
        print(idx)
        # 索引之间差 1 就说明是相连的
        curL = 1
        for i in range(1, len(idx)):
            if idx[i] - idx[i - 1] == 1:
                curL += 1
                res = max(res, curL)
            else:
                curL = 1

        return 0 if curL == 1 else res


s = Solution()
print(s.longestValidParentheses(s="(()"))
print(s.longestValidParentheses(s=")()())"))
print(s.longestValidParentheses("())()()((((())))))()()()()())))"))

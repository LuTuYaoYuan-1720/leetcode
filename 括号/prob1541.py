# coding:utf-8

class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == '(':
                stack.append(s[idx])
            else:
                # 栈里没有 ( 可匹配
                if len(stack) == 0:
                    # 看当前 ) 后边有没有 ) ，如果有，则只要一个 (，并跨过下一位 )
                    if idx + 1 < len(s) and s[idx + 1] == ')':
                        res += 1
                        idx += 1
                    # 没有就需要 左边一个 ( 右边一个 )
                    else:
                        res += 2
                # 栈里有 ( 可匹配
                else:
                    # 看当前 ) 后边有没有 ) ，如果有，栈里弹出一个 (，跨过下一位 )
                    if idx + 1 < len(s) and s[idx + 1] == ')':
                        idx += 1
                        stack.pop()
                    # 当前 ) 后边没有 )，就补一位 )
                    else:
                        res += 1
                        stack.pop()
            idx += 1
        # 栈里最后只剩下 (
        return res + len(stack) * 2

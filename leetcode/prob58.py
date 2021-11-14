# coding=utf-8

"""
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
示例 1：
输入：s = "Hello World"
输出：5
示例 2：
输入：s = "   fly me   to   the moon  "
输出：4
示例 3：
输入：s = "luffy is still joyboy"
输出：6
"""


class Solution(object):
    # def lengthOfLastWord(self, s: str):
    #     s_list = s.split()
    #     return len(s_list[len(s_list) - 1])

    def lengthOfLastWord(self, s: str):
        count = 0
        for i in range(-1, 0 - len(s)-1, -1):
            if s[i] != ' ':
                count += 1
            elif s[i] == ' ' and count != 0:
                break
        return count


if __name__ == '__main__':
    s = "a"
    solution = Solution()
    print(solution.lengthOfLastWord(s))

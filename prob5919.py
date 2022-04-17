# coding:utf-8
class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        pre_cnt = [0] * (len(word) + 1)
        sign = 0
        for i in range(len(word)):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                sign += 1
                pre_cnt[i + 1] = sign
            else:
                pre_cnt[i + 1] = sign

        for l in range(1, len(word) + 1):
            for i in range(0 + 1, len(word) - l + 1 + 1):
                count += pre_cnt[i + l - 1] - pre_cnt[i - 1]
        return count


s = Solution()

print(s.countVowels('aba'))
print(s.countVowels('abc'))
print(s.countVowels('ltcd'))
print(s.countVowels('noosabasboosa'))

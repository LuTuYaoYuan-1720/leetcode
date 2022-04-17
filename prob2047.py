# coding:utf-8
class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        words = sentence.split(' ')

        for word in words:
            if len(word) == 0:
                continue
            sign1 = True
            sign2 = False
            sign3 = False
            lianzifu = 0
            lianzifuindex = -1
            biaodian = 0
            biaodianindex = -1
            for i in range(len(word)):
                if not word[i].islower():
                    if word[i] not in ['-', '!', '.', ',']:
                        sign1 = False
                if word[i] == '-':
                    lianzifu += 1
                    lianzifuindex = i
                if word[i] in ['!', '.', ',']:
                    biaodian += 1
                    biaodianindex = i

            if lianzifu == 1:
                if 0 < lianzifuindex < len(word) - 1:
                    if word[lianzifuindex - 1].islower() and word[lianzifuindex + 1].islower():
                        sign2 = True
            elif lianzifu == 0:
                sign2 = True

            if biaodian == 1:
                if biaodianindex == len(word) - 1:
                    sign3 = True
            elif biaodian == 0:
                sign3 = True

            if sign1 and sign2 and sign3:
                res += 1

        return res


s = Solution()
print(s.countValidWords("cat and  dog"))
print(s.countValidWords("!this  1-s b8d!"))
print(s.countValidWords("alice and  bob are playing stone-game10"))

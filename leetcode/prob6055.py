# coding:utf-8

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curtime = int(current[:2]) * 60 + int(current[3:])
        corrtime = int(correct[:2]) * 60 + int(correct[3:])

        target = abs(curtime - corrtime)
        times = [60, 15, 5, 1]
        i = 0
        sign = [0] * 4
        while target != 0:
            sign[i] = target // times[i]
            target = target % times[i]
            i += 1

        return sum(sign)

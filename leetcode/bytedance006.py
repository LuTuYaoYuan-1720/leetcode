# coding:utf-8

"""
4 100
100 73 60
100 89 35
30 21 30
10 8 10

3 100
100 100 60
80 80 35
21 21 30

2 100
100 30 35
140 140 100
"""


class solution:
    def __init__(self):
        self.n, self.x = map(int, input().split())
        self.info = []
        self.res = 0

    def input(self):
        self.info.append([0] * 3)
        for i in range(self.n):
            tmp = input().split(' ')
            self.info.append([int(i) for i in tmp])

        self.DFS(1, 0, 0, 0)

    def DFS(self, curIndex, curMoney, curYouHui, curKuaiLe):
        if curYouHui >= curMoney - self.x:
            self.res = max(self.res, curKuaiLe)

        if curIndex == len(self.info):
            return

        for i in range(curIndex, len(self.info)):
            self.DFS(i + 1, curMoney + self.info[i][1], curYouHui + self.info[i][0] - self.info[i][1],
                     curKuaiLe + self.info[i][2])


s = solution()
s.input()
print(s.res, end="")

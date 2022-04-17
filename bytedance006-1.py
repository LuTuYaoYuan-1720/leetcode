# n, x = input().split()
# n = int(n)
# x = int(x)
inp = []
with open("./inputs.txt", "r") as f:
    a = f.readlines()
    for i in a:
        inp.append(i.split('\n')[0])
    print(inp)
n = int(inp[0].split()[0])
x = int(inp[0].split()[1])
gameList = []
for i in range(1, n + 1):
    b = inp[i].split()
    gameList.append([int(b[0]), int(b[1]), int(b[2]), int(b[0]) - int(b[1])])
res = float('-inf')
for i in range(n):
    cost = gameList[i][1]
    cut = gameList[i][3]
    happy = gameList[i][2]
    if x - cost <= cut:
        res = max(res, happy)
    for j in range(i + 1, n):
        cost += gameList[j][1]
        cut += gameList[j][3]
        happy += gameList[j][2]
        if cost - x <= cut:
            res = max(res, happy)
        else:
            cost -= gameList[j][1]
            cut -= gameList[j][3]
            happy -= gameList[j][2]
print(res)

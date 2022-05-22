# coding:utf-8

class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.merged = []

    def add(self, left: int, right: int) -> None:
        self.intervals.append([left, right])
        self.intervals.sort(key=lambda x: x[0])

        self.merged = []
        for interval in self.intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not self.merged or self.merged[-1][1] < interval[0]:
                self.merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                self.merged[-1][1] = max(self.merged[-1][1], interval[1])

    def count(self) -> int:
        cnt = 0
        for pair in self.merged:
            cnt += pair[1] - pair[0] + 1
        return cnt


intervals = [[2, 3], [7, 10], [5, 8]]
intervals.sort(key=lambda x: x[0])

merged = []
for interval in intervals:
    # 如果列表为空，或者当前区间与上一区间不重合，直接添加
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        # 否则的话，我们就可以与上一区间进行合并
        merged[-1][1] = max(merged[-1][1], interval[1])

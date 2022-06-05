# coding:utf-8
import random
from typing import List
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        random_x = float('%.5f' % random.uniform(self.x - self.r, self.x + self.r))
        random_y = float('%.5f' % random.uniform(self.y - self.r, self.y + self.r))
        while math.sqrt(abs(random_x - self.r) ** 2 + abs(random_y - self.r) ** 2) >= self.r:
            random_x = float('%.5f' % random.uniform(self.x - self.r, self.x + self.r))
            random_y = float('%.5f' % random.uniform(self.y - self.r, self.y + self.r))
        return [random_x, random_y]


s = Solution(1.0, 0.0, 0.0)
s.randPoint()

print('%.5f' % random.uniform(0, 1))

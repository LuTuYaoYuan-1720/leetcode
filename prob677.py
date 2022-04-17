# coding:utf-8

class MapSum:

    def __init__(self):
        self.m = {}

    def insert(self, key: str, val: int) -> None:
        self.m[key] = val

    def sum(self, prefix: str) -> int:
        cnt = 0

        for k, v in self.m.items():
            if k.startswith(prefix):
                cnt += v

        return cnt

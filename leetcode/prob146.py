# coding:utf-8
import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            value = self.cache.get(key)
            self.cache.pop(key)
            self.cache[key] = value
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.pop(key)
        elif len(self.cache.keys()) == self.capacity:
            fir = list(self.cache.keys())[0]
            self.cache.pop(fir)

        self.cache[key] = value


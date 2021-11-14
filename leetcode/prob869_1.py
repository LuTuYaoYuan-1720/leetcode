# coding:utf-8

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
               524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
               536870912]

        cnts = [0] * 10
        while n != 0:
            cnts[int(n % 10)] += 1
            n /= 10
            n = int(n)

        for num in arr:
            cntnum = [0] * 10
            while num != 0:
                cntnum[int(num % 10)] += 1
                num /= 10
                num = int(num)
            if cntnum == cnts:
                return True

        return False


s = Solution()
print(s.reorderedPowerOf2(10))

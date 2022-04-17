class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)

        counts = []
        for i in arr:
            count = 0
            for num in arr:
                if abs(num - i) % x == 0:
                    count += abs(num - i) / x
                else:
                    break
            if count > 0:
                counts.append(count)

        if len(counts) > 0:
            return int(min(counts))
        else:
            return -1


s = Solution()
print(s.minOperations(grid=[[2, 4], [6, 8]], x=2))
print(s.minOperations(grid=[[1, 5], [2, 3]], x=1))
print(s.minOperations(grid=[[1, 2], [3, 4]], x=2))

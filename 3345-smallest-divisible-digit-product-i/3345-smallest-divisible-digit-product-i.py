class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, n + 100):
            product = 1
            for d in str(num):
                product *= int(d)
            if product % t == 0:
                return num
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)

        # First copy of each item grants its free copies once
        for i, (_, price) in enumerate(items):
            if price <= budget:
                val = 1 + bonus[i]
                for b in range(budget, price - 1, -1):
                    if dp[b - price] + val > dp[b]:
                        dp[b] = dp[b - price] + val

        # Additional copies of each item grant 1 copy each
        for _, price in items:
            if price <= budget:
                for b in range(price, budget + 1):
                    if dp[b - price] + 1 > dp[b]:
                        dp[b] = dp[b - price] + 1

        return max(dp)

    def maxItems(self, items: List[List[int]], budget: int) -> int:
        return self.maximumSaleItems(items, budget)
from collections import defaultdict
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        if not items or budget <= 0:
            return 0

        cheapest = min(price for _, price in items)
        max_factor = max(factor for factor, _ in items)

        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(2 * f, max_factor + 1, f):
                    freq[f] += freq[multiple]

        cost_count = defaultdict(int)
        for factor, price in items:
            bonus_pairs = freq[factor] - 1
            if bonus_pairs > 0 and price <= 2 * cheapest:
                cost_count[price] += bonus_pairs

        total = 0
        rem = budget
        for price in sorted(cost_count):
            if rem < price:
                break
            take = min(cost_count[price], rem // price)
            total += 2 * take
            rem -= take * price

        total += rem // cheapest
        return total
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Sort nodes by nums value, keep original indices
        order = sorted(range(n), key=lambda i: nums[i])
        rank = [0] * n
        for pos, node in enumerate(order):
            rank[node] = pos  # rank[i] = position of node i in sorted order

        # Step 2: Build sorted_nums for easy access
        sorted_nums = [nums[order[i]] for i in range(n)]

        # Step 3: Build "next reachable" in sorted order using two pointers
        # nxt[pos] = furthest position reachable in ONE hop from position pos
        nxt = [0] * n
        right = 0
        for left in range(n):
            right = max(right, left)
            while right + 1 < n and sorted_nums[right + 1] - sorted_nums[left] <= maxDiff:
                right += 1
            nxt[left] = right

        # Step 4: Binary Lifting - precompute jump[k][pos]
        # jump[k][pos] = position reachable from pos in 2^k hops
        LOG = 17  # 2^17 > 10^5
        jump = [[i for i in range(n)] for _ in range(LOG)]
        jump[0] = nxt  # 2^0 = 1 hop

        for k in range(1, LOG):
            for pos in range(n):
                jump[k][pos] = jump[k-1][jump[k-1][pos]]

        # Step 5: Answer queries using binary lifting
        def min_distance(u, v):
            pu, pv = rank[u], rank[v]
            if pu > pv:
                pu, pv = pv, pu  # ensure pu <= pv

            # Check if connected at all
            if nxt[pu] < pv:
                # Try jumping to see if we can reach pv
                pass

            steps = 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][pu] < pv:
                    pu = jump[k][pu]
                    steps += (1 << k)

            # One more step needed?
            if pu != pv:
                if nxt[pu] >= pv:
                    steps += 1
                else:
                    return -1

            return steps

        return [min_distance(u, v) for u, v in queries]
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [0] * (2 * n)
        tree_pref = [[0] * k for _ in range(2 * n)]
        
        for i in range(n):
            idx = n + i
            val = nums[i] % k
            tree_prod[idx] = val
            tree_pref[idx][val] = 1
            
        for i in range(n - 1, 0, -1):
            left = i << 1
            right = left | 1
            tree_prod[i] = (tree_prod[left] * tree_prod[right]) % k
            
            pref = tree_pref[i]
            lp_pref = tree_pref[left]
            for j in range(k):
                pref[j] = lp_pref[j]
                
            lp = tree_prod[left]
            rp = tree_pref[right]
            for v in range(k):
                if rp[v]:
                    pref[(lp * v) % k] += rp[v]

        res = []
        left_nodes = []
        right_nodes = []
        
        for index, value, start, x in queries:
            idx = n + index
            val = value % k
            tree_prod[idx] = val
            pref = tree_pref[idx]
            for j in range(k):
                pref[j] = 0
            pref[val] = 1
            
            idx >>= 1
            while idx > 0:
                left = idx << 1
                right = left | 1
                tree_prod[idx] = (tree_prod[left] * tree_prod[right]) % k
                
                curr_p = tree_pref[idx]
                lp_pref = tree_pref[left]
                for j in range(k):
                    curr_p[j] = lp_pref[j]
                    
                lp = tree_prod[left]
                rp = tree_pref[right]
                for v in range(k):
                    if rp[v]:
                        curr_p[(lp * v) % k] += rp[v]
                
                idx >>= 1
                
            L = start + n
            R = n - 1 + n
            
            left_nodes.clear()
            right_nodes.clear()
            
            while L <= R:
                if L & 1:
                    left_nodes.append(L)
                    L += 1
                if not (R & 1):
                    right_nodes.append(R)
                    R -= 1
                L >>= 1
                R >>= 1
                
            curr_pref = [0] * k
            curr_prod = 1
            
            for node in left_nodes:
                rp = tree_pref[node]
                for v in range(k):
                    if rp[v]:
                        curr_pref[(curr_prod * v) % k] += rp[v]
                curr_prod = (curr_prod * tree_prod[node]) % k
                
            for node in reversed(right_nodes):
                rp = tree_pref[node]
                for v in range(k):
                    if rp[v]:
                        curr_pref[(curr_prod * v) % k] += rp[v]
                curr_prod = (curr_prod * tree_prod[node]) % k
                
            res.append(curr_pref[x])
            
        return res
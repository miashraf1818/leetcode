from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # Segment tree arrays
        pref = [0] * (4 * n)
        suf = [0] * (4 * n)
        max_ans = [0] * (4 * n)
        arr = list(s)
        
        def push_up(node: int, L: int, R: int):
            mid = (L + R) // 2
            left = 2 * node + 1
            right = 2 * node + 2
            
            # Base values from children
            pref[node] = pref[left]
            suf[node] = suf[right]
            max_ans[node] = max(max_ans[left], max_ans[right])
            
            # If the characters at the boundary merge
            if arr[mid] == arr[mid + 1]:
                # Update max length bridging across the middle
                max_ans[node] = max(max_ans[node], suf[left] + pref[right])
                
                # If the entire left segment is identical, the prefix spans into the right
                if pref[left] == (mid - L + 1):
                    pref[node] = pref[left] + pref[right]
                    
                # If the entire right segment is identical, the suffix spans into the left
                if suf[right] == (R - mid):
                    suf[node] = suf[right] + suf[left]

        def build(node: int, L: int, R: int):
            if L == R:
                pref[node] = suf[node] = max_ans[node] = 1
                return
            mid = (L + R) // 2
            build(2 * node + 1, L, mid)
            build(2 * node + 2, mid + 1, R)
            push_up(node, L, R)

        def update(node: int, L: int, R: int, idx: int):
            # Base case: we reached the exact leaf node
            if L == R:
                # The actual character update in `arr` happens before the function is called
                # so the leaf values are just 1s
                return
            
            mid = (L + R) // 2
            if idx <= mid:
                update(2 * node + 1, L, mid, idx)
            else:
                update(2 * node + 2, mid + 1, R, idx)
                
            push_up(node, L, R)

        # 1. Build the initial segment tree
        build(0, 0, n - 1)
        
        ans = []
        # 2. Process each query
        for char, idx in zip(queryCharacters, queryIndices):
            if arr[idx] != char:
                arr[idx] = char
                update(0, 0, n - 1, idx)
                
            # The root of the segment tree always contains the max length for the whole string [0, n - 1]
            ans.append(max_ans[0])
            
        return ans
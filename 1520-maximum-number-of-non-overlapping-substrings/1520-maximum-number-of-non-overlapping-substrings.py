class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Step 1: Precompute the first and last occurrence of each character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        def get_valid_end(start_idx: int) -> int:
            """
            Checks if starting at start_idx forms a valid independent substring block.
            Returns the end index of the block if valid, or -1 if invalid.
            """
            char = s[start_idx]
            end_idx = last[char]
            
            j = start_idx
            while j <= end_idx:
                curr_char = s[j]
                
                # If a character inside our range forces the block to start earlier,
                # this start_idx is not the optimal/minimal start for this block.
                if first[curr_char] < start_idx:
                    return -1
                
                # Extend the required end boundary if necessary
                end_idx = max(end_idx, last[curr_char])
                j += 1
                
            return end_idx

        # Step 2: Collect all valid intervals
        intervals = []
        for char in set(s):
            start = first[char]
            end = get_valid_end(start)
            
            if end != -1:
                intervals.append((start, end))
                
        # Step 3: Greedy Interval Scheduling
        # Sort primarily by end index (to maximize non-overlapping substrings)
        # Secondarily by length (end - start) to minimize total length on ties
        intervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        
        ans = []
        last_end = -1
        
        for left, right in intervals:
            # If the current valid substring doesn't overlap with our previously selected ones
            if left > last_end:
                ans.append(s[left:right + 1])
                last_end = right
                
        return ans
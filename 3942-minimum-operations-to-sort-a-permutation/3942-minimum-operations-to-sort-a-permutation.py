from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Identify the state of the input array
        idx = nums.index(0)
        
        # Check if it matches the normal (non-reversed) cyclic shift pattern
        is_normal = True
        for i in range(n):
            if nums[i] != (i - idx + n) % n:
                is_normal = False
                break
                
        # Check if it matches the reversed cyclic shift pattern
        is_reversed = True
        for i in range(n):
            if nums[i] != (idx - i + n) % n:
                is_reversed = False
                break
        
        # Determine target state to look up
        if is_normal:
            target_state = (0, idx)
        elif is_reversed:
            target_state = (1, idx)
        else:
            return -1  # Impossible configuration
            
        # 2. BFS from the sorted state (0, 0) to find shortest path to all states
        # dist[(rev, idx)] stores the minimum operations
        dist = {}
        queue = deque([(0, 0)])
        dist[(0, 0)] = 0
        
        while queue:
            rev, curr_idx = queue.popleft()
            curr_dist = dist[(rev, curr_idx)]
            
            # If we reached our target state configuration, return the distance immediately
            if (rev, curr_idx) == target_state:
                return curr_dist
                
            # Transition 1: Inverse of Rotate Left (Rotate Right)
            next_idx1 = (curr_idx + 1) % n
            state1 = (rev, next_idx1)
            if state1 not in dist:
                dist[state1] = curr_dist + 1
                queue.append(state1)
                
            # Transition 2: Inverse of Reverse (Reverse)
            next_idx2 = n - 1 - curr_idx
            state2 = (1 - rev, next_idx2)
            if state2 not in dist:
                dist[state2] = curr_dist + 1
                queue.append(state2)
                
        return dist.get(target_state, -1)
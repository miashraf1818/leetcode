from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build adjacency list (directed graph)
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        
        # Step 1: BFS/DFS from k to find all suspicious methods
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    queue.append(nei)
        
        # Step 2: Check if any non-suspicious method invokes a suspicious one
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                # Can't remove! Return all methods
                return list(range(n))
        
        # Step 3: Safe to remove — return all non-suspicious methods
        return [m for m in range(n) if m not in suspicious]
         
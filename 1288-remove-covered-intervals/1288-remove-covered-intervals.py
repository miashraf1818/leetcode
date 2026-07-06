class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, if equal sort by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        removed = 0
        max_end = 0
        
        for start, end in intervals:
            if end <= max_end:
                removed += 1
            else:
                max_end = end
        
        return len(intervals) - removed
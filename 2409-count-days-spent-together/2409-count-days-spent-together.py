class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_days(date_str: str) -> int:
            m, d = map(int, date_str.split('-'))
            return sum(days[:m-1]) + d
            
        a1 = to_days(arriveAlice)
        a2 = to_days(leaveAlice)
        b1 = to_days(arriveBob)
        b2 = to_days(leaveBob)
        
        start = max(a1, b1)
        end = min(a2, b2)
        
        return max(0, end - start + 1)
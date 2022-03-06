class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            x1, y1 = intervals[i - 1]
            x2, y2 = intervals[i]
            if x2 < y1:
                return False
            
        return True
            
        
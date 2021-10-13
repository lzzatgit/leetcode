class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        elif len(intervals) == 1:
            return 1

        # when len(intervals) >= 2:
        intervals.sort(key = lambda x: x[0])
        free_rooms = []
        free_rooms.append(intervals[0][1])

        for meeting in intervals[1:]:
            min_end_time = min(free_rooms)
            if min_end_time <= meeting[0]:
                free_rooms.remove(min_end_time)
            free_rooms.append(meeting[1])

        return len(free_rooms)

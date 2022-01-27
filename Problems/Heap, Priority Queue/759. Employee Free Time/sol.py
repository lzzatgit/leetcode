import heapq
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        all_interval = []
        res = []

        for i in range(len(schedule)):
            all_interval += schedule[i]

        all_interval = sorted(all_interval, key = lambda x: x.start)
        end_time = all_interval[0].end

        for j in range(len(all_interval)):
            cur_interval = all_interval[j]
            if cur_interval.start <= end_time:
                end_time = max(end_time, cur_interval.end)
            else:
                free_interval = Interval(start = end_time, end = cur_interval.start)
                res.append(free_interval)
                end_time = cur_interval.end
        return res

# time O(NlogN)
# space O(N)

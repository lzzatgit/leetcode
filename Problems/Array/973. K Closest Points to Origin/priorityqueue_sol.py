from queue import PriorityQueue

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        q = PriorityQueue()
        res = []


        def calculate_dist(pos):
            return sqrt((pos[0])**2 + (pos[1])**2)

        for p in points:
            dist = calculate_dist(p)
            q.put((dist, p))

        for i in range(k):
            res.append(q.get()[1])

        return res

# time O(nlogn)
# space O(n)

from queue import PriorityQueue
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        q = PriorityQueue()
        res = []
        hashtable = Counter(nums)

        # O(nlogn)
        for key, value in hashtable.items(): # O(n)
            q.put((-1*value, key)) # O(log(n))

        for i in range(k):
            res.append(q.get()[1]) # O(1)

        return res

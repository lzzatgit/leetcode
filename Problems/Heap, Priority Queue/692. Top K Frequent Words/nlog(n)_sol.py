import heapq, collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = collections.Counter(words)

        heap = [(-freq, word) for word, freq in hashmap.items()] # in python heapq is min heap so we need to use -freq in order to find the most frequent items

        heapq.heapify(heap)

        res = [heapq.heappop(heap)[1] for i in range(k)]

        return res

# time O(nlogn) when creating the heap with size n
# space O(n)

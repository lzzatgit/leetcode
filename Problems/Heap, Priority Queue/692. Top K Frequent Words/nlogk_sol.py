import heapq, collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashtable = collections.Counter(words)
        return heapq.nsmallest(k, hashtable, key = lambda word: (-hashtable[word], word))

# time O(nlogk)

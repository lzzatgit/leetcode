import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [] # minheap
        n = len(matrix) # row num
        m = len(matrix[0]) # col num
        counter = 0

        # create a heap with size of min(N, K)
        for i in range(min(n, k)):
            heap.append((matrix[i][0], i, 0))
        heapq.heapify(heap) # O(logn)

        while counter < k:
            ele, row, col = heapq.heappop(heap) # O(1)
            if col < m-1:
                heapq.heappush(heap, (matrix[row][col+1], row, col+1)) # O(logn)
            counter += 1

        return ele

# leetcode Solution
# time O()

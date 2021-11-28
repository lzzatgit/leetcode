class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x):
            return x[0]**2 + x[1]**2

        def partition(i, j): # quick sort algorithm
            pivot = points[j]
            l = i - 1
            for r in range(i, j):
                rp = points[r]
                if dist(rp) < dist(pivot):
                    l += 1
                    points[l], points[r] = points[r], points[l]
            points[j], points[l+1] = points[l+1], points[j]
            return l+1

        def sort(i, j, k):
            if i >= j: return

            mid = partition(i, j)
            if mid - i + 1 == k: return
            elif mid - i + 1 < k:
                sort(mid+1, j, k - (mid - i + 1) )
            else:
                sort(i, mid-1, k)

        sort(0, len(points)-1, k)
        return points[:k]

# sol: https://www.youtube.com/watch?v=G9VcMTSZ1Lo&t=1357s

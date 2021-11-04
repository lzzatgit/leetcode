class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        if len(arr) == k:
            return arr

        min_dist = float('inf')
        n_found = 0

        #fist use bi-search once to find the smallest element
        while l <= r:
            mid = (l + r) // 2
            if arr
                

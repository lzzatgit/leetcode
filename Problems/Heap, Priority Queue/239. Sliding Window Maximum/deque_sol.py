from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0 # left and right boundry of the window
        res = []
        q = deque()

        # notice here that the queue we are maintaining is a monotonically decreasing queue so from left to right the elements can only be in decreasing order. So when compare we compare from the right side and also remove from the right size. So line 10 and 11.
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < l: # need to throw elements that are no longer in the window
                q.popleft()

            if r + 1 >= k: # r is idx so need to plus 1 before compared to k
                res.append(nums[q[0]]) # since monotonically decreasing queue so the left most element is the largest one
                l += 1
            r += 1

        return res

# https://www.youtube.com/watch?v=DfljaUwZsOk
# time O(N) since we access each element exactly twice. All deque operation are O(1)
# space O(N)

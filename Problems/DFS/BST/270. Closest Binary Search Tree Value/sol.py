# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        cur_closest = root.val
        shortest_dist = float('inf')

        def dfs(node):
            nonlocal cur_closest, shortest_dist
            if not node:
                return
            diff = node.val - target
            if abs(diff) < shortest_dist:
                shortest_dist = abs(diff)
                cur_closest = node.val

            if diff > 0: # node.val > target
                dfs(node.left) # search in the left side
            if diff < 0:
                dfs(node.right)

        dfs(root)
        return cur_closest

# time O(h) since BST attribute, no need to visit each node once
# space O(h) since recursion

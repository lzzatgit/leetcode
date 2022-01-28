# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val # init value

        # This finction will return max path sum if split is not allowed at root
        def dfs(root):
            if not root: # base case
                return 0

            nonlocal res # declare the global variable

            left_max_sum = dfs(root.left)
            right_max_sum = dfs(root.right)

            left_max_sum = max(left_max_sum, 0) #in case the left_max_sum is negative
            right_max_Sum = max(right_max_sum, 0)

            potential_max_sum = left_max_sum + right_max_Sum + root.val
            res = max(res, potential_max_sum)

            return max(left_max_sum+root.val, right_max_Sum+root.val)

        dfs(root)
        return res

# https://www.youtube.com/watch?v=Hr5cWUld4vU
# time O(N) casue visit each node exactly once
# space O(h) where h is the height of the Tree
        

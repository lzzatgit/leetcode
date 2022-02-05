# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return node

            if node.left:
                dfs(node.left)

            if node.val >= low and node.val <= high:
                res += node.val

            if node.right:
                dfs(node.right)

        dfs(root)

        return res

# time O(n)
# space O(h)

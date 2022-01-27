# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        right = TreeNode()
        left = TreeNode()

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left

        return root

# leetcode recursion Solution
# time O(n) cause each node is visited once
# space O(h) where h is the height of the tree

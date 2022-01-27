# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diamemter = 0

        def longest_length(node):
            if not node:
                return 0

            nonlocal diamemter

            left_length = longest_length(node.left)
            right_length = longest_length(node.right)

            diamemter = max(diamemter, left_length+right_length)

            return max(left_length, right_length) + 1

        longest_length(root)
        return diamemter

# leetcode sol
# time O(N)
# space avg O(logN) worst case O(N), depends on the height of the tree 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        successor = None

        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor

# leetcode Solution
# time O(N) for skewed tree and O(logN) for a balanced tree
# space O(1)

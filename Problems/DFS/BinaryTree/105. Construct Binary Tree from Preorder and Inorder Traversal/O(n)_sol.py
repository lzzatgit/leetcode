# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(left, right):
            nonlocal preorder_idx
            if left > right:
                return

            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            root.left = dfs(left, hashtable[root.val] -1)
            root.right = dfs(hashtable[root.val] + 1, right)
            return root

        hashtable = {ele:idx for idx, ele in enumerate(inorder)}

        preorder_idx = 0

        return dfs(0, len(inorder) - 1)

# leetcode sol
# time O(n)
# space O(n)

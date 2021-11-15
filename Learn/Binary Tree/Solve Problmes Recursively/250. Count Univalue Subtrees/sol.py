# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        self.count = 0
        self.uniVal(root)
        return self.count

    def uniVal(self, root):
        if root.left == None and root.right == None: #base case
            self.count += 1
            return True

        is_uni = True
        if root.left != None:
            is_uni = self.uniVal(root.left) and is_uni and root.val == root.left.val

        if root.right != None:
            is_uni = self.uniVal(root.right) and is_uni and root.val == root.right.val
        self.count += is_uni

        return is_uni

# from leetcode solution
# time: O(n) casue visit each node
# space: O(H) H is the height of the tree

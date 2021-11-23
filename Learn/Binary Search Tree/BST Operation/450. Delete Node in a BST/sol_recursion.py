# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor_val(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor_val(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor_val(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor_val(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

# leetcode Solution
# Time O(H) when balanced tree O(logN) because H = logN
# space O(H) to keep the recursion stack

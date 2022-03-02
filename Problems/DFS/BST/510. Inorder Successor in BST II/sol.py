"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return None

        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor

        while node.parent and node == node.parent.right:
            node = node.parent

        return node.parent

# leetcode Solution
# time O(H) where H is the height of the tree, O(N) worst case
# space O(1)

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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        p2 = q

        while p1 != p2:
            if not p1.parent:
                p1 = q
            else:
                p1 = p1.parent
            if not p2.parent:
                p2 = p
            else:
                p2 = p2.parent

        return p1

# time O(depth of p + depth of q - depth of LCA) where n is the number of node in the tree
# space O(1) only created two pointers and no recursion

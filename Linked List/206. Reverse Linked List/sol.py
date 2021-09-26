# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode()

        while head:
            prehead.next, head.next, head = head, prehead.next, head.next

        return prehead.next

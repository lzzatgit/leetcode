# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"), head)
        m_prev = self.findkth(dummy, left-1)
        m = m_prev.next
        n = self.findkth(dummy, right)
        n_next = n.next
        n.next = None

        self.reverse(m)
        m_prev.next = n
        m.next = n_next

        return dummy.next

    def findkth(self, head, k):
        for i in range(k):
            head = head.next
        return head

    def reverse(self, head):
        prev = None
        while head is not None:
            next_head = head.next
            head.next = prev
            prev = head
            head = next_head
        return prev

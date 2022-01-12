# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        m_prev = self.findKth(dummy, left - 1)
        m = m_prev.next
        n = self.findKth(dummy, right)
        n_next = n.next
        n.next = None # this is very important, to seperate the sublist from the main list, otherwise will reverse everything after m

        self.reverse(m)

        # connect the head and tail correspondingly
        m_prev.next = n
        m.next = n_next

        return dummy.next

    def findKth(self, head, k):
        for i in range(k):
            head = head.next
        return head

    def reverse(self, head):
        prev = None

        while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next

        return prev

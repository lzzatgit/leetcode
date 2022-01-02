# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # end condition
        if not head or not head.next:
            return head

        # find the middle point of the linked list, and break the linked lst to two
        slow_prev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow_prev = head if not slow_prev else slow_prev.next
        slow = slow_prev.next
        slow_prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        prehead = ListNode()
        prev = prehead

        # merge sort
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next # remember to update prev pointer

        # append to tail is anything left
        prev.next = l1 if l2 is None else l2

        return prehead.next

# time: O(NlogN)
# space: O(logN)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddsHead = ListNode(0)
        evensHead = ListNode(0)
        odds = oddsHead
        evens = evensHead

        isodd = True

        while head:
            if isodd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isodd = not isodd
            head = head.next

        evens.next = None
        odds.next = evensHead.next

        return oddsHead.next

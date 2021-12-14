# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # find the middle of the linked list (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # start to reverse the 2nd half of the linked list, starting slow
        # after reverse, prev is the start
        prev = None
        while slow:
            next_head = slow.next
            slow.next = prev
            prev = slow
            slow = next_head

        # check palindrome
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True

# https://www.youtube.com/watch?v=yOzXms1J6Nk
# time O(n)
# space O(1)

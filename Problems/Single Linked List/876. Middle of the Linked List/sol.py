# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return

# 记住这个快慢指针的方法返回的是（当奇数个）中点，（当偶数个）最中间两个的第二个

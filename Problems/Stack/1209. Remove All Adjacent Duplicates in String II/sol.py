class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cnt_stack = []

        for i in s:
            last = None if not stack else stack[-1]
            if i != last:
                stack.append(i)
                cnt_stack.append(1)

            else: #if i == last
                cnt_stack.append(cnt_stack.pop() + 1)

            if cnt_stack[-1] == k:
                stack.pop()
                cnt_stack.pop()

        res = ''
        for j in range(len(stack)):
            res = stack.pop() * cnt_stack.pop() + res

        return res

# leetcode sol comment
# time O(n)
# space O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        self.helper(n, n, '', res)
        return res

    def helper(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helper(l-1, r, item+'(', res)
        if r > 0:
            self.helper(l, r-1, item+')', res)

# recursion idea, https://www.youtube.com/watch?v=XF0wh8M2A6E
# time O()
# space O()

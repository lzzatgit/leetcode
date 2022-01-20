class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        opt = '+'
        res = 0

        while i < len(s):
            # number
            if s[i] >= '0' and s[i] <= '9':
                num = 0
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1

            # +
            if s[i] in '+-*/' or i == len(s)-1:
                if opt == '+':
                    stack.append(num)
                elif opt == '-':
                    stack.append(-num)
                elif opt == '*':
                    stack.append(stack.pop()*num)
                elif opt == '/':
                    stack.append(int(stack.pop()/num))
                opt = s[i]

            i += 1

        for i in stack:
            res += i

        return res

# leetcode sol 1

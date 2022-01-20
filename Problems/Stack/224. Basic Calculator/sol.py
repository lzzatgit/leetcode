class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_sum = 0
        sign = 1
        i = 0

        while i < len(s):
            # when i is a number:
            if (s[i] >= '0' and s[i] <= '9'):
                num = 0
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    num = num * 10 + int(s[i])
                    i += 1
                cur_sum += sign * num
                i -= 1

            elif s[i] == "+":
                sign = 1

            elif s[i] == "-":
                sign = -1

            elif s[i] == "(":
                stack.append(cur_sum)
                stack.append(sign)
                cur_sum = 0
                sign = 1

            elif s[i] == ")":
                cur_sum = stack.pop() * cur_sum #this pops the sign
                cur_sum += stack.pop()

            i += 1

        return cur_sum

# https://www.youtube.com/watch?v=081AqOuasw0

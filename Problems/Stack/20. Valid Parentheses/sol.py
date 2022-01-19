class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []

        for i in s:
            if len(parentheses) == 0:
                parentheses.append(i)
            else:
                top = parentheses[-1]
                if (top == "(" and i == ")") or (top == "[" and i == "]") or (top == "{" and i == "}"):
                    parentheses.pop()
                else:
                    parentheses.append(i)

        if len(parentheses) == 0:
            return True
        return False

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        idx_to_remove = set() # 用set不用list是因为最后check元素在不在list里面O(n)但set是O(1)
        string_builder = []

        for idx, ele in enumerate(s):
            if ele not in "()": # ele is letter
                continue
            if ele == "(":
                stack.append(idx)
            elif not stack: # when ele == ")" and stack is empty
                idx_to_remove.add(idx)
            else:
                stack.pop()

        idx_to_remove = idx_to_remove.union(stack)

        for idx, ele in enumerate(s):
            if idx not in idx_to_remove: #这一步如果idx_to_remove是list那这个for loop就是O(n**2)而不是O(n)了,需要注意
                string_builder.append(ele)

        return ''.join(string_builder)

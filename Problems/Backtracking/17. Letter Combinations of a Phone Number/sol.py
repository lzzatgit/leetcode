class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        if n == 0:
            return res

        letter_dict = {
            "2" :"abc",
            "3" :"def",
            "4" :"ghi",
            "5" :"jkl",
            "6" :"mno",
            "7" :"pqrs",
            "8" :"tuv",
            "9" :"wxyz"
        }

        def helper(path, idx):
            if len(path) == n:
                res.append("".join(path))
                return
                
            all_letters = letter_dict[digits[idx]]
            for letter in all_letters:
                path.append(letter)
                helper(path, idx+1)
                path.pop()

        helper([], 0)
        return res

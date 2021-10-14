class Solution:

    def lettercounts(self, word):
        letters = []
        counts = []
        for letter in word:
            if not letters or letter != letters[-1]:
                letters.append(letter)
                counts.append(1)
            else:
                counts[-1] += 1
        return letters, counts

    def isStrechy(self, word):

        w_letters, w_counts = self.lettercounts(word)

        if self.s_letters != w_letters:
            return False

        for i in range(len(self.s_letters)):
            if self.s_counts[i] < 3 and self.s_counts[i] != w_counts[i]:
                return False
            if self.s_counts[i] >= 3 and self.s_counts[i] < w_counts[i]:
                return False
        return True

    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        self.s_letters, self.s_counts = self.lettercounts(s)
        for word in words:
            if self.isStrechy(word):
                res += 1

        return res

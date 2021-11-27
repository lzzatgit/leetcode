class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0

        for num in nums:
            deno = 1
            dgt_cnt = 0
            while num // deno > 0:
                deno *= 10
                dgt_cnt += 1

            if dgt_cnt % 2 == 0:
                cnt += 1
        return cnt

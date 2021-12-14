class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num):
            res = 0
            while num > 0:
                digit = num % 10
                num = num // 10
                res += digit ** 2

            return res

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

        

class Solution:
    def isHappy(self, n: int) -> bool:

        def sqr(num):
            return sum(int(i) ** 2 for i in str(num))

        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sqr(n)

        return True
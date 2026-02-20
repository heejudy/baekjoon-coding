from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        deq = deque()
        st = str(x)
        for i in st: 
            deq.append(i)
        while len(deq) > 1:
            if deq.popleft() == deq.pop():
                continue
            else:
                return False

        return True
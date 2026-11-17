class Solution:
    def isHappy(self, n: int) -> bool:
        s = {n}
        next = n
        while True:
            next = sum(int(x)**2 for x in str(next))
            if next == 1:
                return True
            if next in s:
                return False
            s.add(next)
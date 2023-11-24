# https://leetcode.com/problems/base-7/submissions/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        base = 0
        i = 1
        x = num / abs(num)
        num = abs(num)
        while num != 0:
            r = num % 7
            num //= 7
            base += r * i
            i *= 10
        return str(int(base*x))
        
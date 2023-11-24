# https://leetcode.com/problems/power-of-four/submissions/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n,4) == int(math.log(n,4))
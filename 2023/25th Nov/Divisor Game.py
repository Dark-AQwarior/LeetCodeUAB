# https://leetcode.com/problems/divisor-game/description/
# Alice and Bob take turns playing, n % x == 0 and if so then n-x

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
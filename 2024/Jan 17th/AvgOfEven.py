# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        x = 0
        n = 0
        for i in nums:
            if i % 2 == 0:
                if i % 3 == 0:
                    x += i
                    n += 1
        if n == 0:
            return n
        else:
            return int(x/n)
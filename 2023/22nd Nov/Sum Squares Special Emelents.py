# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        squares = 0
        n = len(nums)
        for i in range(0,n):
            if n % (i+1) == 0:
                squares += nums[i] * nums[i]
                print(i," ",squares)
        return squares
        
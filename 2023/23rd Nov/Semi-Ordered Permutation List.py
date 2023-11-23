# https://leetcode.com/problems/semi-ordered-permutation/submissions/

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        if nums[0] == 1 and nums[-1] == len(nums):
            return 0
        c = 0 
        start = nums.index(1)
        end = nums.index(len(nums))
        if start < end:
            c = start + (len(nums) - 1 - end)
        else:
            c = start + (len(nums) - 1 - end) - 1
        return c
        
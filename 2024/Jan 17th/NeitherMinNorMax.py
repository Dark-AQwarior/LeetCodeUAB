# https://leetcode.com/problems/neither-minimum-nor-maximum/description/

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        for i in nums:
            if i != x and i != y:
                return i
        return -1

# single line

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return sorted(nums)[1] if len(nums) > 2 else -1
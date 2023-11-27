# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = 0
        if len(nums) == 3:
            m = max(m, (nums[0] - nums[1]) * nums[2])
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    m = max(m, (nums[i] - nums[j]) * nums[k])

        if m > 0:
            return m
        else:
            return 0

# Optimized code

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        x, y, m = 0, 0, 0
        for i in nums:
            x = max(x, i*y)
            y = max(y, m-i)
            m = max(m, i)
        return x
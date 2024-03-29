# https://leetcode.com/problems/number-of-good-pairs/submissions/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    c+=1
        return c
    
# Optimized using dictionaries

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        d = {}
        for i in nums:
            if i in d:
                c += d[i] # adding the frequency of the identical element
                d[i] += 1
            else:
                d[i] = 1
        return c
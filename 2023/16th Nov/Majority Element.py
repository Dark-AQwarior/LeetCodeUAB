# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = {}
        for i in range(0,n):
            if nums[i] not in res:
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1
        
        for i in res.keys():
            if res[i] > n//2 :
                return i
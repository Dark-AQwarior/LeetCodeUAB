# https://leetcode.com/problems/number-of-arithmetic-triplets/description/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c = 0
        for i in range(0, len(nums)):
            j = nums[i] - diff
            k = nums[i] + diff
            if j in nums and k in nums:
                c+=1
        return c
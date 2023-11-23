# https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n > 0:
            nums = [0,1]
        else:
            nums = [0]
        for i in range(2, n+1):
            if i % 2 == 0:
                nums.append(nums[i//2])
            else:
                nums.append(nums[i//2]+nums[(i//2)+1])
        print(nums)
        return max(nums)
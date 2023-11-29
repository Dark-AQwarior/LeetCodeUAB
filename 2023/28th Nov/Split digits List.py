# https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            for j in str(i):
                answer.append(int(j))
        return answer
    
# 2nd way

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            l = []
            while i > 0:
                l.append(i%10)
                i//=10
            answer += l[::-1]
        return answer
    

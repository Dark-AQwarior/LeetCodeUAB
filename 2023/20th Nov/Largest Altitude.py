# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l = [0]
        for i in range(1,len(gain)+1):
            l.append(l[i-1]+gain[i-1])
        return max(l)
    
# Using temp

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l = 0
        m = 0
        for i in range(1,len(gain)+1):
            l+=gain[i-1]
            m = max(m,l)
        return m
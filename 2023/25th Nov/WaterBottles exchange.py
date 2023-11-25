# https://leetcode.com/problems/water-bottles/submissions/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s = 0
        while numBottles >= numExchange:
            floor = numBottles // numExchange
            s += floor * numExchange
            numBottles = floor + numBottles % numExchange
        s += numBottles
        return s
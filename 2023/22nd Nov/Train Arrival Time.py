# https://leetcode.com/problems/calculate-delayed-arrival-time/submissions/

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        arrival = arrivalTime + delayedTime
        if arrival >= 24:
            arrival = arrival - 24
        return arrival
        
# Optimized code

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
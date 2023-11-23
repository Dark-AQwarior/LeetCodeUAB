# https://leetcode.com/problems/distance-between-bus-stops/submissions/

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start > destination:
            start, destination = destination, start
        startToDestinationSum = sum(distance[start:destination])
        distancesSum = sum(distance)
        return min(distancesSum-startToDestinationSum,startToDestinationSum)
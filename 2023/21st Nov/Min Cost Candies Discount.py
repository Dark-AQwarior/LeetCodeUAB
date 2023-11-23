# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/submissions/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        mcost = 0
        while len(cost) > 0:
            if len(cost) > 1:
                mcost += cost[-1] + cost[-2]
                if len(cost) >= 3:
                    cost = cost[:-3]
                else:
                    cost = cost[:-2]
            else:
                mcost += cost[-1]
                cost = cost[:-1]
        return mcost
    
# Optimal Solution

class Solution:
    
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        mcost = 0
        for i in range(-1, -(len(cost)+1), -1):
            if i%3 == 0:
                continue
            mcost += cost[i] 
            
        return mcost

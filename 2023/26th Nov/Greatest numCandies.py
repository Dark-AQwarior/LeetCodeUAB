# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        o = []
        for i in range(0,len(candies)):
            x = candies[i] + extraCandies
            o.append(x >= max(candies))
        return o        
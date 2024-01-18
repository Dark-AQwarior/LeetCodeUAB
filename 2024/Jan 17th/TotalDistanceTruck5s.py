# https://leetcode.com/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        x = 0
        if mainTank < 5:
            return mainTank * 10
        while mainTank > 0:
            if mainTank >= 5:
                x += mainTank - 5 + 1
                print(x, mainTank)
                mainTank -= 5
                x += 5
        return x*10
# https://leetcode.com/problems/check-if-it-is-a-straight-line/submissions/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, len(coordinates)):
            if ((y2-y1)*(coordinates[i][0] - x1)) != ((coordinates[i][1] - y1)*(x2-x1)):
                return False
        return True
        
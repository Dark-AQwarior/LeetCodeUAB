# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l1 = ['a','c','e','g']
        l2 = ['b','d','f','h']

        if coordinates[0] in l1:
            if int(coordinates[1]) % 2 == 0:
                return True
            else:
                return False
        else:
            if int(coordinates[1]) % 2 == 0:
                return False
            else:
                return True
            
# Optimized Solution

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - int(coordinates[1])) % 2 == 0:
            return False
        else:
            return True
        
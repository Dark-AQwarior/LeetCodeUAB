# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/submissions/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
# rstrip is used remove suffix character occurences of a string
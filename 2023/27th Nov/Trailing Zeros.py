# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/submissions/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')
# rstrip is used remove suffix character occurences of a string

# Another code
# converting string to integer so that 0's at end are gone, returning string again
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        s = int(num[::-1])
        return str(s)[::-1]
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        for i in range(0, len(t)):
            if c >= len(s):
                break
            if s[c] == t[i]:
                c+=1
        return c == len(s)
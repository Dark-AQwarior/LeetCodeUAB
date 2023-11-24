# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/submissions/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s = []
        for i in range(0, len(s2)):
            if s1[i] != s2[i]:
                s.append(i)
        if len(s) < 2:
            return False
        else:
            s2 = s2[:s[0]] + s2[s[1]] + s2[s[0] + 1:s[1]] + s2[s[0]] + s2[s[1] + 1:]
        return s1 == s2
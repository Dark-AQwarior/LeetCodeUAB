# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        t = 0
        n = len(min(strs, key=len))
        for i in range(0, n):
            if t == 1:
                break
            for j in range(0, len(strs)):
                if strs[0][i] in strs[j][i]:
                    continue
                else:
                    t = 1
                    break
            if t == 0:
                s += strs[0][i]
        return s
        
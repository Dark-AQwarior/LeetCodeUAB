# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/submissions/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        l = ''
        for i in words:
            l += i[0]
        return l == s
        
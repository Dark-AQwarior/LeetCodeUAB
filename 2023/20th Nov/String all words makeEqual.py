# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = {}
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if words[i][j] not in c:
                    c[words[i][j]] = 1
                else:
                    c[words[i][j]] += 1
        val = list(c.values())
        count = 0
        for i in range(0,len(val)):
            if val[i] % len(words) != 0:
                return False
        return True
        
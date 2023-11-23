# https://leetcode.com/problems/counting-words-with-a-given-prefix/submissions/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c = 0
        for i in range(0, len(words)):
            if words[i].startswith(pref):
                c+=1
        return c
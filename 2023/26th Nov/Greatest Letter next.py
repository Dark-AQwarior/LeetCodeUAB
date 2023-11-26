# https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = sorted(letters)
        for i in letters:
            if ord(i) > ord(target):
                return i
        return letters[0]
        
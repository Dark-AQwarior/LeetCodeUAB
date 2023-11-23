# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in range(1,len(s)+1):
            if s[-i] == " ":
                continue
            else:
                c+=1
                if -i-1 >= -len(s) and s[-i-1] == " ":
                    break
        return c
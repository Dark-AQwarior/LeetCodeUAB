# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            if i.isalnum():
                s1+=i.lower()
        print(s1)
        return s1[::-1] == s1        
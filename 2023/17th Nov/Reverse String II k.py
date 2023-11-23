# https://leetcode.com/problems/reverse-string-ii/description/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s2 = ''

        for i in range(0,len(s),2*k):
            s1 = s[i:k+i]
            s2 += s1[::-1]+s[k+i:i+2*k]
        
        return s2
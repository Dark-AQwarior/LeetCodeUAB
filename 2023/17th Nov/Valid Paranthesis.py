# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if s[i] == ')' and bool(stack):
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif s[i] == ']' and bool(stack):
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}' and bool(stack):
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not bool(stack)
    
# Optimized code

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_brackets = ['[]', '()', '{}']
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if bool(stack):
                    bracket_pair = stack[-1] + s[i]
                    if bracket_pair in valid_brackets:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not bool(stack)
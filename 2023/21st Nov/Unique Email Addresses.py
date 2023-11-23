# https://leetcode.com/problems/unique-email-addresses/description/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()

        for email in emails:
            at = email.find('@')
            newEmail = ''
            plus = email.find('+')
            for i in range(0,len(email)):
                if email[i] == '.' and i < at:
                    continue
                elif email[i] == '+':
                    continue
                elif plus != -1 and i > plus and i < at:
                    continue
                else:
                    newEmail += email[i]
            
            valid.add(newEmail)
        return len(valid)
    
# Optimal Solution

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()

        for email in emails:
            x, y = email.split('@')
            x1 = x.split('+')[0].replace('.','')
            valid.add(x1+'@'+y)
        return len(valid)
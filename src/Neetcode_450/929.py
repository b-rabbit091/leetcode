'''

# Use regex to clean email
cleaned_email = re.sub(r'\.(?=[^@]+@)', '', email)         # Remove dots before @
cleaned_email = re.sub(r'\+[^@]+', '', cleaned_email)
'''

import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        em_set = set()
        for email in emails:
            local, domain = email.split('@')
            local = re.sub(r'\+.*', '', local)
            local = local.replace('.', '')
            cleaned_email = f'{local}@{domain}'
            em_set.add(cleaned_email)
        return len(em_set)


sol = Solution()
emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails))

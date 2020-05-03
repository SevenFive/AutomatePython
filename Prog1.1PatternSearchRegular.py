#   The same pattern find as in Prog1PatternSearchNoRegular but with regular expression

import re  # to use regular expression

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.')
print(mo.group())

#   or all results with use of '.findall'
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'))

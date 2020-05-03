#   regex groups and pipe character

import re
#   displaying part of the result separately
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-391-2323.')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
#   or searching for '(415)'
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex2.search('My number is (415) 391-2323.')
print(mo2.group(1))

# pipe for multiple search of variations
batRegex = re.compile(r'bat(man|mobile|copter|bat)')
mo3 = batRegex.findall('Batman was using his batmobile for the last two years without batcopter or batdriver. It was alwayts about batabat things.')
print(mo3)
#   if the pattern is not found the result will be NONE which creates error for .group() method.

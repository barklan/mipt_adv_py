import re
p = re.compile(r'([ab]{1}) \1')
print(p.search('ab asb fd'))

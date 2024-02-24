import re
p = re.compile('[A-Z][a-z]+')
m = p.findall('Ali Zhanzakov')
print(m)

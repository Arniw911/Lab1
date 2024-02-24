import re 
p = re.compile('ab*')
m = p.search('abb')
print(m.group())
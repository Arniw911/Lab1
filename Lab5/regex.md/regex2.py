import re 
p = re.compile('ab{2,3}')
m = p.search('abbbb')
print(m.group())
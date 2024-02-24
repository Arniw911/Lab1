import re 
p = re.compile('a.*b')
m = p.search('aEYIGпF799697hh$%(*hfybbbab')
print(m.group())
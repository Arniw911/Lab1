#1
import re 
p = re.compile('ab*')
m = p.search('abb')
print(m.group())

#2
import re 
p = re.compile('ab{2,3}')
m = p.search('abbbb')
print(m.group())

#3
import re
p = re.compile('[a-z]+_[a-z]+')
m = p.findall('gh_hdh_h_d_d_happyd')
print(m)

#4
import re
p = re.compile('[A-Z][a-z]+')
m = p.findall('Ali Zhanzakov')
print(m)

#5
import re 
p = re.compile('a.*b')
m = p.search('aEYIGпF799697hh$%(*hfybbbab')
print(m.group())

#6
import re 
string = "jshfo.solkfhd sjfoih,, ioshdf"
find = '[ .,]'
replacement = ":"
replaced = re.sub(find, replacement, string)
print(replaced)

#7
import re 
string = "camel_string"
replaced = re.sub('_[a-z]', lambda match: match.group()[1].upper(), string)
print(replaced) 

#8
import re 
string = "whiteSpaceWord"
replaced = re.split('[A-Z]', string)
print(replaced) 

#9
import re 
string = "whiteSpaceWord"
replaced = re.sub('[a-z][A-Z]', lambda match: match.group()[0] + ' ' + match.group()[1], string)
print(replaced) 

#10
import re 
string = "snakeCase"
replaced = re.sub('[a-z][A-Z]', lambda match: match.group()[0] + '_' + match.group()[1].lower(), string)
print(replaced)
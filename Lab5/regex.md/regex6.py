import re 
string = "jshfo.solkfhd sjfoih,, ioshdf"
find = '[ .,]'
replacement = ":"
replaced = re.sub(find, replacement, string)

print(replaced) 
import re 
string = "whiteSpaceWord"

replaced = re.sub('[a-z][A-Z]', lambda match: match.group()[0] + ' ' + match.group()[1], string)

print(replaced) 
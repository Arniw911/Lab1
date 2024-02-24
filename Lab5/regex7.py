import re 
string = "camel_string"

replaced = re.sub('_[a-z]', lambda match: match.group()[1].upper(), string)

print(replaced) 
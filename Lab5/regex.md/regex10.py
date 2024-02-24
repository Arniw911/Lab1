import re 
string = "snakeCase"

replaced = re.sub('[a-z][A-Z]', lambda match: match.group()[0] + '_' + match.group()[1].lower(), string)

print(replaced)
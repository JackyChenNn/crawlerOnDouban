import re
pattern = 'something'
string = 'something'

prog = re.compile(pattern)
result = prog.match(string)
print(result)

pattern = 's.*g'
string = 'something'

prog = re.compile(pattern)
result = prog.match(string)
print(result)
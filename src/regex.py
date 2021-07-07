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

print(re.match('.*@.*\.com','123@123.com'))
print(re.match('(.*)@(.*\.com)','123@123.com').group(1))
print(re.match('(.*)@(.*\.com)','123@123.com').group(2))

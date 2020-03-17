import re

a = re.compile('\d').findall('ddd')
print(len(a))
import re

x = re.sub(r'\s|\.|\,', ":", input())
print(x)
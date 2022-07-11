import re

str = "China is a great country"
x = re.findall(".*a", str)
print(x)
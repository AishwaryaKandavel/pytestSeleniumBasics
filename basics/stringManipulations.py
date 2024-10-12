from operator import concat

str1: str = 'Aishwarya'
str2: str = 'Elavarasan'
str3: str = ' loves '

print(str1[3])
print(str2[0:9])
print(concat(str1, str2))
print(str1[0:5] in str1)
print(str1.split('a'))
print(str1.split('q'))
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())
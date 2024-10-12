from turtledemo.forest import doit1
from typing import TextIO, List

file = open('file.txt')
print(file.read(), "\n")
file.close()
file1 = open('file.txt')
print(file1.read(5), "\n")
file1.close()
print(open('file.txt').read())

print(open('file.txt').readline())

file3: TextIO = open('file.txt')
flag: bool = True
while flag:
    line: str = file3.readline()
    if line=="":
        flag = False
    print(line)
file3.close()

file4: TextIO = open('file.txt')
lines: list[str] = file4.readlines()
for file in lines:
    print(file)
file4.close()

with open('file.txt') as reader:
    lines: list[str] = reader.readlines()
    with open('file.txt', 'w') as writer:
        for line in reversed(lines):
            writer.write(line)
print(open('file.txt').readlines())
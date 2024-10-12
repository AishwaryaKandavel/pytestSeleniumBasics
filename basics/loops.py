list = [1, 2, "a", "huh87y", 3.4]
#advanced for loop
for i in list:
    print(i)
#no increment value
for i in range(0, len(list)):
    print(list[i])
    print(list[i],"...")
#all conditions
for i in range(0, len(list), 2):
    print(list[i])
#no first index and increment value
for i in range(len(list)):
    print(list[i], i)

a = 10
while a>0:
    if a%2==0:
        print(a,"divisible by 2")
    if a%3==0:
        a = a - 1
        continue
    if a == 2:
        break
    a = a - 1
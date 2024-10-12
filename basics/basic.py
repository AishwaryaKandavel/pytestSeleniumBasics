print("hello")
a = 3
print(a)
s = "hi"
print(s)
f = 0.1
print(f)
b, c, d = 5, 6.5, "String"
print(b, c, d)
#no space format
print("{}{}".format(b,d))

#list - mutable
values = [1, 2.0, "Ela", "Aish"]
print(values[0])
print(values[-1])
print(values[2:4])
values.insert(3, 10)
values.append(10.0)
print(values)
del values[-1]
values[1] = 10
print(values)

#tuple - immutable
a = (1, 2, 3, 4, "Ela")
print(a[1])
print(a)

#dictionary
a = {1:"firstname", 2:"lastname", 3:"age", "id":123}
print(a[1])
print(a["id"])
print(a)

dict = {}
dict[1] = "ela"
dict[2] = "aish"
print(dict)
print(dict[1])
# #list.py
# list = [4 ,"ali" , "alina" , "blue" , 4, 8 , True]
# print(list[0])

# #we ca change do changes in list even string yes, they are immutable
# list[0] = 5
# print(list[0])
# print(list[0:4])
# print(list)

# #methods we ca change do changes in list even string yes, they are immutable
# list = [2 , 5, 78, 2 , 1]
# list.sort()
# print(list)

# list.insert(3 ,10)
# print(list)

# print(list.pop(0))
# print(list)

# list.remove(2)
# print(list)

# list.reverse()
# print(list)

# #03_tupple.property
# a = (1, 2, 3, 4, 5, 7, "ali", False) #pathar ki lakeeer can't change
# print(a)
# print(type(a))

# #tuple_methods.py,

a = ("a", "ghi" , "b", "c" ,"d" ,1, 2, 3)
b = a.index("a")
print(b)

no = a.count(3)  #3 kitny time aya hy
print(no)

c = a * 3
print(c)

print(a is a)

print(len(a))

a = (1 , 2 , 3)
a , b, c = a
print(a , b, c)   2 15 mint ki video
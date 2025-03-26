my_list = []
i = 1
my_list.extend(i * 10 for i in range(1, 5))
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50,60,70])
print(my_list)
my_list.pop(-1)
print(my_list)
print(my_list.index(30))
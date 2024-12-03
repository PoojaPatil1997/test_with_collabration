# # my_list = ["Apple", "Banana", "orange"]
# # brothers_list = {'idk': 'azad', 'idk2': 'azad1'}
# # my_list.extend(brothers_list.values())
# # print(my_list)
# # print(["Apple", "Banana", "orange"]*5)
# print(list(range(1, 6)) * 3)

list1 = [1, 2, 3, 4, 5]
list2 =list1[:]
print(list1)
print(list2)
list2[0] = 10
print(list1)
print(list2)
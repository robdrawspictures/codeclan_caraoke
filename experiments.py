from gettext import find


list1 = ["rob", "bob", "bobby", "roberto", "bert", "bobby", "pat"]
list2 = []
list3 = [1, 2, 3, 2, 2, 4, 5]
list4 = []

# list2.append(list1[0])

print(list1)
print(list2)
print(list3)
print(list4)

def find_matching(old_list, name, new_list):
    for item in old_list:
        if item == name:
            new_list.append(item)

# def find_matching_numbers(name):
#     for item in list3:
#         if item % name == 0:
#             list4.append(item)

# Actually finds all numbers divisible by name, because
# I can do maths, but I figured out why the other function
# wasn't doing what I wanted, anyway. (Passing the wrong list).

find_matching(list1, "bobby", list2)
find_matching(list3, 2, list4)
print(list1)
print(list2)
print(list3)
print(list4)

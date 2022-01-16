from gettext import find


list1 = ["rob", "bob", "bobby", "roberto", "bert", "bobby", "pat"]
list2 = []
list3 = [1, 2, 3, 2, 2, 4, 5]
list4 = []

# list2.append(list1[0])

# print(list1)
# print(list2)
# print(list3)
# print(list4)

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

# find_matching(list1, "bobby", list2)
# find_matching(list3, 2, list4)
# print(list1)
# print(list2)
# print(list3)
# print(list4)

ratings = {"S" : "10", "A" : "8", "B" : "6",
        "C" : "4", "D" : "2", "F" : "0"
        }

# for key, value in ratings.items():
#     print(key)
#     print(value)

# for key, value in ratings.items():
#     if key == "S":
#         print(value)

singing_ability = "A"
print(singing_ability)

# def convert_ability_to_int(ability):
for key, value in ratings.items():
    if key == "A":
        singing_ability = value


# convert_ability_to_int(singing_ability)
print(singing_ability)

singing_ability2 = "S"
print(singing_ability2)

def convert_ability_to_int(ability):
    print(f"Previous: {ability}")
    for key, value in ratings.items():
        if key == ability:
            globals()[ability] = value
    print(f"Current: {ability}")

convert_ability_to_int(singing_ability2)
print(singing_ability2)

# singing_ability3 = "F"
# print(singing_ability3)

# def brute_force():
#     global singing_ability3
#     singing_ability3 = 0

# brute_force()
# print(singing_ability3)

# message = "Old Variable"

# def global_var(variable):
#     global variable
#     variable = "New Variable"
#     print(variable)
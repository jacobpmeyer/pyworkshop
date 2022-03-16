names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
print(my_list)
[4, 3, 4, 5]

print("Before", my_list)

my_list = [len(name) for name in names]
print("After", my_list)

my_list = [num for num in range(0, 100) if num % 2 == 0]
print(my_list)

import random
my_dict = {num:random.randint(0, 100) for num in my_list}
print(my_dict)

my_set = {num for num in my_dict.values()}
print(my_set)

# Files are exectuted on import
if __name__ == "__main__":
    print("Henlo")

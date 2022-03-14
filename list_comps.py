names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
print(my_list)
[4, 3, 4, 5]

print("Before", my_list)

my_list = [len(name) for name in names]
print("After", my_list)

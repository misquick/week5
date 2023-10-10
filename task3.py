input_string = input("Enter a string: ")

num_count = 0
upper_count = 0
lower_count = 0
other_count = 0

for char in input_string:
    if char.isdigit():
        num_count += 1
    elif char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    else:
        other_count += 1

print("Number of numbers:", num_count)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
print("Number of other characters:", other_count)

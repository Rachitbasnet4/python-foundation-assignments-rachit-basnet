'''
Exercise 3: Clean Numeric Values
Name: Rachit Basnet
Day 2
'''

# input list
raw_values = [100, None, 250, "invalid", 300, None, 450]

# empty list
cleaned_values = []

# looping through each value in the list
for value in raw_values:
    # skiping values that are not int
    if not isinstance(value, int):
        continue

    # adding value to cleaned value list
    cleaned_values.append(value)

# output
print(cleaned_values)

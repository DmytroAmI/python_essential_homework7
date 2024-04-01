my_list = [1, 2, 3, 4, 5]

generate = (item for item in my_list[::-1])
print(type(generate))
print(list(generate))

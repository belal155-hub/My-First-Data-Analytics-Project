data_list = [30, 54, 12, 15, 67, 100, 56, 90, 85, 98, 10]
new_list = []

while data_list:
    minimum = data_list[0]
    for x in data_list:
        if x > minimum:
            minimum = x

    new_list.append(minimum)
    data_list.remove(minimum)

print(new_list)
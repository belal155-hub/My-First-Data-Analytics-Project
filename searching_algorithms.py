def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

numbers = [1, 2, 3, 4, 4, 5, 5, 6, 1]
result = search(numbers, 10)

if result != -1:
    print("Present in the list")

else:
    print("Absent in the list")
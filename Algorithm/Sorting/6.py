# Library Sort
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)

array.sort()
print(array)

arr = [('banana', 2), ('apple', 5), ('carrot', 3)]


def setting(data):
    return data[1]


result = sorted(arr, key=setting)
print(result)

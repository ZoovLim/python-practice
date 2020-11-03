# Quick Sort
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(a, start, end):
    if start >= end:
        return
    pivot = partition(a, start, end)
    quick_sort(a, start, pivot - 1)
    quick_sort(a, pivot + 1, end)


# Partition
def partition(a, start, end):
    last_small = start
    for i in range(start + 1, end + 1):
        if a[i] < a[start]:
            last_small += 1
            a[last_small], a[i] = a[i], a[last_small]
    a[start], a[last_small] = a[last_small], a[start]
    return last_small


quick_sort(array, 0, len(array) - 1)
print(array)

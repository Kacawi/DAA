from math import floor

def sort_count(array):

    n2 = floor(len(array) / 2)

    if len(array) == 1: 
        return array, 0

    else:
        b, x = sort_count(array[0:n2])
        c, y = sort_count(array[n2:])
        d, z = merge_count_split(b, c)

    return d, x + y + z

def merge_count_split(b, c):
    result = []
    i = 0
    j = 0
    count = 0

    while i < len(b) and j < len(c): 
        if b[i] <= c[j]:
            result.append(b[i])
            i += 1
        else:
            result.append(c[j])
            j += 1
            count += len(b) - i # Add number of inversions

    while i < len(b):
        result.append(b[i])
        i += 1

    while j < len(c):
        result.append(c[j])
        j += 1

    return result, count

# r, c = sort_count([5, 2, 3, 1, 4])
# print([5, 2, 3, 1, 4], "=> Number of inversions:", c)
# s, d = sort_count([5, 2, 3, 4, 6, 9])
# print([5, 2, 3, 4, 6, 9], "=> Number of inversions:", d)

# Test Array
fd = open('TestIntegerArray.txt')
arr = []
for line in fd:
    arr.append(int(line))

r, c = sort_count(arr)
print("Number of inversions:", c)

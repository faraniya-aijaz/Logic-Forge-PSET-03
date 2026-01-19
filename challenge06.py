def find_repeated(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]

    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 2]:
            return arr[i]

    return arr[0]


nums1 = [2, 1, 2, 5, 3, 2]
print(find_repeated(nums1))


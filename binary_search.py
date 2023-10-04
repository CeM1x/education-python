def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        if guess > num:
           high = mid - 1
        else:
            low = mid + 1
    return None

arr = [1,2,3,4,5,6]
print(arr)
print(binary_search(arr, 2))

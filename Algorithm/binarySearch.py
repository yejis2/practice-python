def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = start + (end - start) // 2
        if key == arr[middle]:
            return True
        elif key < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False


# 재귀함수
def binarySearch2(arr, low, high, key):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == arr[middle]:
            return True
        elif key < arr[middle]:
            return binarySearch2(arr, low, middle - 1, key)
        else:
            return binarySearch2(arr, middle + 1, high, key)


def arrayBinarySearch(low, high, target, array):
    print (f"{low};{high}")
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return arrayBinarySearch(mid + 1, high, target, array)
        return arrayBinarySearch(low, mid - 1, target, array)
    else:
        return -1


if __name__ == "__main__":
    list = list(range(1, 11))
    print(list)
    target = 1
    x = arrayBinarySearch(0, len(list) - 1, target, list)
    print(f"index of target {target}= {x}")

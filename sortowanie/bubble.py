def bubble_sort(Arr):
    for i in range(0, len(Arr) - 1):
        j = 0
        while j < len(Arr)-1 :

            if Arr[j] > Arr[j + 1]:
                # temp = Arr[j + 1]
                # Arr[j + 1] = Arr[j]
                # Arr[j] = temp
                Arr[j+1],Arr[j] = Arr[j],Arr[j+1]

            j += 1
    return Arr


if __name__ == "__main__":
    Arr = [5, 4, 3, 2, 1]
    result = bubble_sort(Arr)
    print(result)

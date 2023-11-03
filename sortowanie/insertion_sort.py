import itertools


def insertion_sort(arr):
    for i in range(1, len(arr)):
        print (arr)
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            print(f"-->{key}...{arr}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":

    arr = [6, 5, 3, 2, 4,1]
    insertion_sort(arr)
    print("Sorted array:", arr)
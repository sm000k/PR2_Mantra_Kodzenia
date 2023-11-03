def insertionsort(arr):
    for i in range(0, len(arr) - 1):
        key = arr[i]
        for j in range(len(arr) - 1, -1, -1):
            if(key < arr[j])



if __name__ == "__main__":
    arr = list(range(10, 0, -1))
    # range jest niepoważny bo nei sięga liczby będącej stopem
    print(arr)
    insertionsort(arr)

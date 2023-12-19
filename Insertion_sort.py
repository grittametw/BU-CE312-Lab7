num = [11,4,7,5,10,9,13,1]
print("Ex.array :", num)

def insertionSort(arr):

    z = 1

    for i in range(1, len(arr)):

        key = arr[i]
        s = i - 1

        while s >= 0 and key < arr[s]:
            arr[s + 1] = arr[s]
            s -= 1

        arr[s + 1] = key
        print("Step %d:" %z, arr)
        z += 1

    return arr

result = insertionSort(num)
print("Sorted array :", result)
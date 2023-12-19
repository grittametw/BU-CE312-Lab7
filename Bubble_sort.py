num = [11,4,7,5,10,9,13,1]
print("Ex.array :", num)

def bubblesort(arr):

    z = 1
    
    for i in range(len(arr)-1):
        
        for s in range(len(arr)-1):
            
            if arr[s] > arr[s+1]:
                tmp = arr[s]
                arr[s] = arr[s+1]
                arr[s+1] = tmp
                print("Step %d:" %z, num)
                z += 1

    return arr

result = bubblesort(num)
print("Sorted array :", result)
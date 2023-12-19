num = [11,4,7,5,10,9,13,1]
print("Ex.array :", num)

def selectionSort(arr,size):
	
    z = 1
    
    for i in range(size):
        min_index = i
        
        for s in range(i + 1,size):
            
            if arr[s] < arr[min_index]:
                min_index = s

        print("Step %d:" %z, arr)
        z += 1
      
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

    return arr

size = len(num)
result = selectionSort(num,size)
print("Sorted array :", result)
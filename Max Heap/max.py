def max(arr, j, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < j and arr[i] < arr[l]:
        largest = l
    
    if r < j and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max(arr, j, largest)

def insert(array, Num):
    size = len(array)
    if size == 0:
        array.append(Num)
    else:
        array.append(Num)
        for i in range((size//2)-1, -1, -1):
            max(array, size, i)

def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
        
    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)
    
    for i in range((len(array)//2)-1, -1, -1):
        max(array, len(array), i)
    
arr = []

insert(arr, 17)
insert(arr, 15)
insert(arr, 13)
insert(arr, 16)
insert(arr, 12)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 15)
print("After deleting an element: " + str(arr))
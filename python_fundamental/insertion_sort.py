x=[5,4,6,8,123,75,23,86,97]
def insertionSort(arr):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)-1):
            if(arr[0+i]>arr[j+1]):
                arr[0+i],arr[j+1] = arr[j+1],arr[0+i]
    return arr
print(insertionSort(x))
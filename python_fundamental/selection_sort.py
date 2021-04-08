def selectionSort(arr):
    for j in range(0,len(arr)):
        min=arr[0+j]
        for i in range(j,len(arr)): #this for loop is for finding the smallest
            if arr[i]< min:
                min=arr[i]
        for i in range(j,len(arr)): #after we find the smallest from before, this will swap the smallest with the current next position on the array
            if(arr[i]==min):
                arr[j],arr[i]=arr[i],arr[j]
    return arr

x=[5,4,6,8,123,75,23,86,97]
print(selectionSort(x))    
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(arr):
    for i in range(0, len(arr)):
        if(arr[i]>0):
            arr[i]="big"
    return arr
x=[-1,3,-5,5]
print(biggie_size(x))
# Count Positives - Given a list of numbers, create a function to replace the last value 
# with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(arr):
    count=0
    for i in range(0, len(arr)):
        if(arr[i]>0):
            count+=1
    arr[len(arr)-1]=count
    return arr
x=[1,-2,3,-4,5,-6]
print(count_positives(x))
# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def Sum_total(arr):
    sum=0
    for i in range(0, len(arr)):
        sum+=arr[i]
    return sum
x=[1,2,3,4,5]
print(Sum_total(x))    
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def Average(arr):
    sum=0
    for i in range(0,len(arr)):
        sum+=arr[i]
    avg=sum/len(arr)
    return avg
x=[1,2,3,4,5]
print(Average(x))
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(arr):
    return len(arr)
x=[1,2,3,4,5]
print(length(x))
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(arr):
    if(len(arr)==0):
        return False
    else:
        smallest=arr[0]
        for i in range(0, len(arr)):
            if(arr[i]<smallest):
                smallest=arr[i]
        return smallest
x=[1,-2,3,-4,5]
y=[]
print(minimum(y))
# Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(arr):
    if(len(arr)==0):
        return False
    else:
        biggest=arr[0]
        for i in range(0, len(arr)):
            if(arr[i]>biggest):
                biggest=arr[i]
        return biggest
x=[1,2,3,4,5]
y=[]
print(maximum(x))
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(arr):
    if(len(arr)==0):
        return False
    else:
        sumTotal=0
        minimum=maximum=arr[0]
        for i in range(len(arr)):
            if(arr[i]>maximum):
                maximum=arr[i]
            if(arr[i]<minimum):
                minimum=arr[i]
            sumTotal+=i
        avg=sumTotal/len(arr)
        new_Dict={'sumTotal': sumTotal, 'average': avg, 'minimum': minimum, 'maximum': maximum, 'length': len(arr)}
        return new_Dict
x=[1,2,3,4,5]
print(ultimate_analysis(x))
# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(arr):
    for i in range(0, round(len(arr)/2)):
        temp=arr[i]
        arr[i]=arr[len(arr)-(i+1)]
        arr[len(arr)-(i+1)]=temp
    return arr
x=[1,2,3,4,7]
print(reverse_list(x))
        
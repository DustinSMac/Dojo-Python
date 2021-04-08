x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def changeIT(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if(arr[i][j]==10):
                arr[i][j]=15
    return arr
x = [ [5,2,10], [10,8,9] ]
print(changeIT(x))
# Change the last_name of the first student from 'Jordan' to 'Bryant'
def change_last_name(arr):
    arr[0]['last_name']='Bryant'
    return arr
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}]
print(change_last_name(students))
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def Andres(dict):
    for val in dict:
        for i in range(0,len(dict[val])):
            if(dict[val][i]=="Messi"):
                dict[val][i]="Andres"
    return dict
x=Andres(sports_directory)
print(x)
# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
def change20(list):
    for i in range(0,len(list)):
        for j in list[i]:
            if(list[i][j]==20):
                list[i][j]=30
    return list
print(change20(z))

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the associated value. 
# For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(arr):
    for i in range(0,len(arr)):
        y=[]
        for key, val in arr[i].items():
            x=f"{key} - {val}"
            y.append(x)
        print(", ".join(y))
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, the function prints the value stored 
# in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key,arr):
    for i in range(0,len(arr)):
        for k,val in arr[i].items():
            if(k==key):
                print(val)
iterateDictionary2('last_name',students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and 
# then prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    for i in dict:
        print(f"{len(i)} {i.upper()}")
        for j in range(0,len(dict[i])):
            print(dict[i][j])
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
#1
def a():
    return 5
print(a())
#Output should be 5
#2
def a():
    return 5
print(a()+a())
#Output should be 10
#3
def a():
    return 5
    return 10
print(a())
#Output should be 5. return 5 already ended the function.
#4
def a():
    return 5
    print(10)
print(a())
#Output should be 5. same as above, return 5 already ended the function
#5
def a():
    print(5)
x = a() # 5 was printed out since function a() was called.
print(x) # x has nothing attached, therefore should print out none.
#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#should be error or none, since a(1,2) has no value, and a(2,3) also had no value.
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#Output should be 25, which is a string and not integer
#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#Output should be 100, 10.
#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #7
print(a(5,3)) #14
print(a(2,3) + a(5,3)) #21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) #8 is the output
#11
b = 500
print(b) #500 is the output
def a():
    b = 300
    print(b)
print(b) #500 is the output
a() #300 is the output
print(b)#500 is the output.
# in total, output should be 500,500,300,500.
#12
b = 500
print(b) #500
def a():
    b = 300
    print(b)
    return b
print(b) #500
a() #300. if a() was assigned to a new variable, that variable will now be 300
print(b) #500.
#output should be 500,500,300,500
#13
b = 500
print(b)#500
def a():
    b = 300
    print(b)
    return b
print(b)#500
b=a()#as I was saying from above, now b was assigned to be 300, but before that, 300 was printed since a() was called.
print(b) #300
#total output should be 500,500,300,300
#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # since a() was called, 1 will be printed first. then b() was called inside a(), which means 3 will be printed, then 2 will be printed
#total output should be 1,3,2
#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a() # since a() was called, 1 will be printed, then b() was called inside a(), which means 3 will be printed
#and 5 was assigned to x on a(), so now 5 will be printed.
print(y) #should print out 10
#total output should be 1,3,5,10

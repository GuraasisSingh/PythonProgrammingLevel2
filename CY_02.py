#Session 2

#gui to calculate factorial of a number.
#take string as input and display it with a message/
#build gui to take user details nd checkwhether he is eligible to vote or not
#build gui to take three numbers and perform all arithmetic operations on them

#create a function to calculate simple interest
#create a class to store employee records like employee name, employee number, employee salary
#create a function to calculate compound interest
#create a class to store purchase details with appropriate fields

#gui to compute area of different shapes
#build a python gui to calculate pythagora and eucladian and manhattan distance.

'''
Recursion ::

def recurse():
    ....
    recurse()
    ....
recurse()

def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return(x*fact(x-1))
n=int(input("Enter the number: "))
print("The factorial of", n,"is",fact(n))
'''
#fibonnaci series
def f(n):
    if n<=1:
        return n
    else:
        return (f(n-1)+f(n-2))
nt=10
if nt<=0:
    print("INVALID")
else:
    for i in range(nt):
        print(f(i))
    


                

#OOPs

#Advantages:
#Modularity principle
#standard working modules -> makes our work easier
#very scalable
#easily classified

#Disadvantages:
#length of program becomes higher
#takes time to compile again and again
#takes time to understand
#a brilliant programming skill is required

'''
Applications:
Its helps us to design real time system design.
It can be used neural networking.
It is used in office automation system.
AI expert system
Clint server system.(OCSI)->oop, clint server and internet
ODMS(Data Management)


HW's
Revise OOP System and inheritence.

'''
#Function:
"""
Lambda Functions:
function without a name, any number of arguments

Syntax:
lambda arguments:expression

cube=lambda x:x*x*x
print(cube(5))

a=[(lambda x:x*2)(x) for x in range(5)]
print(a)

x=lambda a:a+10
print(x(2))

y=lambda a,b,c:a+b+c
print(y(2,4,5))

def a(n):
    return lambda a:a*n
d=a(2)
print(d(4))

def s(y):
    return y*y
print(s(4))
ls=lambda y:y*y
print(ls(3))

t=[lambda x=x:x*10 for x in range(1,11)]
for ts in t:
    print(ts())

m=lambda a,b:a if(a>b) else b
print(m(1,2))
"""


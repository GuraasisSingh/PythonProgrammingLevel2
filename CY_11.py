#Different Approaches
'''a=[]
n=int(input("Enter the number of elements in list: "))
for i in range(1,n+1):
    e=int(input("Enter the elements: "))
    a.append(e)
a.sort()
print("Second largest element:",a[-2])
'''
'''
def s(a,al):
    if(al<2):
        print("Invalid Input")
        return
    f=s=-2143242412
    for i in range(al):
        if(a[i]>f):
            s=f
            f=a[i]
        elif(a[i]>s and a[i]!=f):
            s=a[i]
    if(s==-2143242412):
        print("There is no second largest element")
    else:
        print("Second largest element is",s)
a=[12,34,112,455,23,97]
n=len(a)
s(a,n)
'''
def s(b,e,a,n):
    if(b==e):
        c=[0]*n
        c[0]=1
        c[1]=a[b]
        return c
    c1=s(b,(b+e)//2,a,n)
    c2=s((b+e)//2+1,e,a,n)
    if(c1[1]>c2[1]):
        k=c1[0]+1
        c1[0]=k
        c1[k]=c2[1]
        return c1
    else:
        k=c2[0]+1
        c2[0]=k
        c2[k]=c1[1]
        return c2 
def f(e,a):
    c1=s(0,e-1,a,e)
    c2=s(2,c1[0]+2,c1,c1[0])
    print(c2[1])
n=10
a=[1,34,56,23,20,998,1232,45,786,232]
f(n,a)


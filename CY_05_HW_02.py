#2.Use the bubble sort algorithm to sort the numbers in ascending order using last digit of the numbers display result of each step. 

def bs(a):
    s=True
    t=0
    while(s):
        s=False
        for i in range(len(a)-t-1):
            if (a[i]%10) > (a[i+1]%10):
                a[i],a[i+1]=a[i+1],a[i]
            s=True
        t+=1
    print("The number of iterations ",t)
    return a
a=[35,63,88,46,17,42]
print("The unsorted list: ",a)
print("The sorted list: ",bs(a))
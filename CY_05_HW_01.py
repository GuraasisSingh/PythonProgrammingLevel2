#1.Use the bubble sort algorithm to sort the names of ten students in ascending order and display result of each step.

def bs(a):
    s=True
    t=0
    while(s):
        s=False
        for i in range(len(a)-t-1):
            if (a[i]>a[i+1]):
                a[i],a[i+1]=a[i+1],a[i]
            s=True
        t+=1
    print("The number of iterations ",t)
    return a
a=['rohit','rajvir','ramesh','sohan','billy','aman','prashant','kalpit','shraddha','riya']
print("The unsorted list: ",a)
print("The sorted list: ",bs(a))
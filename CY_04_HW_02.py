'''Implement Binary search algorithm to do find the odd numbers within a 
list and replace them if:
They end with 1, replace the entire number with 0
They end with 3, don't do anything
They end with 5, replace the entire number -3
They end with 7, replace them with 2
They end with 9, replace them with 18'''

a=[11,23,85,74,46,8,10,17,59]
t=list(a)
n=len(a)
low=0
high=len(a)-1
while(low<=high):
    i=0
    mid=low+(high-low)//2
    if(a[mid]%2==1):
        if a[i]%10==1:
            a[i]=0
        elif a[i]%10==5:
                a[i]=-3
        elif a[i]%10==7:
                a[i]=2
        elif a[i]%10==9:
                a[i]=18
        break
    elif (a[mid]%2==0):
        low=mid+1
    else:
        high=mid-1
    i+=1
print(t)
print(a)
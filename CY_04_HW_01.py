#Implement binary search algo to find zubair in list of names archana, danny, benny, ishaan, zubair, ram 

def bs(a,x,low,high):
    while(low<=high):
        mid=low+(high-low)//2
        if(a[mid]==x):
            return mid
        elif (a[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1
a=['archana', 'danny', 'benny', 'ishaan', 'zubair', 'ram' ]
x='zubair'
ans=bs(a,x,0,len(a)-1)
print(ans)
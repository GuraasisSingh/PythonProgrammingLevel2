''' 
Merge Sort:
Approach/Principle - Divide and Conquer

A[p..r]
q
A[p...q] and A[q+1,r]

merge function-> merges two parts
merge(arrl,m,r)
arr[l.......m] and arr[m+1.......r]
r>l
m=l+(r-1)/2

algorithm:
def ms(arr,l,r):
    if l>=r:
        return mid = (l+r)//2
    ms(arr,l,mid)
    ms(arr,mid+1,r)
    ms(arr,l,r,mid)

Eg: 
3,1,4,1,5,9,2,6,5,4
'''
def ms(a):
    print("Splitting: ",a)
    if len(a)>1:
        mid=len(a)//2
        lh=a[:mid]
        rh=a[mid:]

        ms(lh)
        ms(rh)
        i=j=k=0
        while i<len(lh) and j<len(rh):
            if lh[i]<rh[j]:
                a[k]=lh[i]
                i+=1
            else:
                a[k]=rh[j]
                j+=1
            k+=1
        
        while i<len(lh):
            a[k]=lh[i]
            i+=1
            k+=1

        while j<len (rh):
            a[k]=rh[j]
            j+=1
            k+=1
    print("Merging:",a)
a=[14,46,43,27,57,41,45,21,70]
ms(a)          
print(a)


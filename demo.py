def findPairs(A,arr_size,sum):
    start=0
    end=arr_size-1

    while start<end:
        if (A[start]+A[end]==sum):
            print(A[start],A[end])
            start+=1
        elif A[start]+A[end]<sum:
            start+=1
        else:
            end-=1
size=int(input("Enter the size"))
A=[]
for i in range(1,size+1):
    A.append(int(input("Enter the elements: ")))
sum=int(input("Enter the largest sum: "))
findPairs(A,len(A),sum)


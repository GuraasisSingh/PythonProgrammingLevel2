"""
Quick Sort :::
Divide and conquer
pivot element selection:rightmost element

arr=[8,7,6,1,0,9,2]

1st pointer -> pivot element (here 2)
2nd pointer -> 8

[8,7,6,1,0,9,2]
[8,7,6,1,0,9,2]
[8,7,6,1,0,9,2]
[1,7,6,8,0,9,2]
[1,0,6,8,7,9,2]


[1,0,2,8,7,9,6]



#HW
[2,5,3,8,6,5,4,7]

Algorithm::
def p(arr, start,end):
    pivot=arr[start]
    low=start+1
    high=end

    while True:
        while low<=high  and arr[high]>=pivot:
            high=high-1

        while low<=high and arr[low]<=pivot:
            low=low+1

        if low<=high:
            arr[low],arr[high],arr[high],arr[low]
        else:
            break
    arr[start],arr[high]=arr[high],arr[start]
    return high
    
"""

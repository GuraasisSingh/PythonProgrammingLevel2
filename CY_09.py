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
'''def partition(l,r,num):
    pivot,pointer=num,r,1
    for i in range(l,r):'''

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot 
def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
def quicksort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values

    return nums

example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quicksort(0, len(example)-1, example))

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
# As you can see, it works for duplicates too
print(quicksort(0, len(example)-1, example))

"""
Linked List:
1.Linear:
2.Non-Linear

a=set(["a","b","c","d"])
print(a)
b=frozenset(["e","f","g","h"])
print(b)
import array
a=array.array("u",['&','*','-','#'])
for i in a:
    print (i)
print(a)

"""
import array
'''
i,b,B,h,H,l,I,q,Q->int
u->unicode character
f,d-> float
'''
a=array.array("i",[1,2,3])
for i in a:
    print (i)
print(a)
a.insert(3,4)#position,element
a.append(56)
print(a)
#Adding elements to array
#insert,append function

#removal of elements->remove,pop
#index->returns first occurence
# Differences in List and Araay
# 1. different datatype in list but same elements in array
# 2. no need of importing module in terms of list but it is impotant in array
# 3. list cannot directly handle arithmetic operations whereas arrays can handle
# 4. list can be nested to contain different types of elements whereas arrays must contain all nested elements of same size
# 5. List is preferred for a shorter sequence of data, and array is preferred for long sequences of data
# 6. Greater flexibility allows easy modification(addition, deletion of data) in list whereas in arrays since less flexible since it is element wise operations.
# 7. The entite list can be printed without any explicit looping, In arrays a loop needs to be formed to access or print components of array
# 8. Consume larger memory for easy addition of elements in lists whereas arrays are more compact in size.

'''
#List
b=[1,"Amit",["a","e"]]
for j in b:
    print(j)
print(b)'''

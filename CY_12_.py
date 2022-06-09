'''Juhi wants to save the contact number of her friends on her mobile phone 
so he created a list of her friends with numbers. 
She decided to sort the list in alphabetical order first then save the number.
 Write a program in python to sort a list using insertion sort.
A school teacher was writing different words on the board in random order. 
Then he told the students to write the words in the correct order as written in the dictionary.
 Write a python program and use the insertion sort algorithm to sort the list of words. 
 Then print all the words of the list in the correct order.'''


def iso(a):
    for i in range(1,len(a)):
        val =a[i]
        j=i-1        
        while j>=0 and val<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=val
        
print("Save the contacts in the following order::")
ContactList=['Rohan','Rahul','Rohit',"Aman","Bunny","Hargun"]
iso(ContactList)
print("List in Alphabetical Order is: ",ContactList)
'''Sakshi thought that if we can use recursion for the repetitive process then definitely 
we can create different shapes as well with the help of recursion instead of using nested loops. 
Sakshi's friend Mansa said it is impossible to print patterns with the help of recursion. 
To prove that printing the following patterns is possible with help of recursion write a python program'''

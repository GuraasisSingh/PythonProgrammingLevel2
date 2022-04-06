 #->Implement linear search algorithm to find 
 # how many no. of times the letter p and s occured in the word mississippi

a='mississippi'
p=0 
s=0
n=len(a)
for i in range(n):
    if a[i] =='p':
        #print('no of times p is increased by 1',p)
        p+=1
    elif a[i] =='s':
        s+=1
print('s',s)        
print('p',p)
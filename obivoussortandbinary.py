# l=[55,65,34,87,98]
# x=[]
# while(len(l)>0):
#     min=l[0]
#     for i in range(len(l)):
#         if l[i]<min:
#              min=l[i]
#     x.append(min)
#     l.remove(min)

# print(x)    
# print(l)

def binar_search(L,k):
"""this function is alternative for the obvious search.It does exactly what is expected 
from the obvious search,but in an efficient way.This method is called the binary search."""
#we want to shrink my list
#we will do that using while loop
begin=0 #first element in L.
end=len(L)-1 #the last element in L is in len(L).L[len(L)-1]
#use a while loop to look at the list and keep halving .
while(end-begin>1):
    #we will handle the case when the number of elements is less than or equal to 1
    mid=(begin+end)//2

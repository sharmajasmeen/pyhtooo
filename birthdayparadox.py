import random
# print(random.random())
# l=[]
# l.append(random.random())
# print(l)
# l.append(random.random())
# print(l)
# for i in range(10):
#     l.append(random.random())
# print(l) #outside the for loop returns one list

# for i in range(100):
#     l.append(random.randint(1,1000))#returns integer
#     #append random numbers betweeen 1 to 1000
#     #append 100 of them
# print(l)
l=[]
for i in range(30):
    l.append(random.randint(1,365))#returns integer
    #append random numbers betweeen 1 to 365
    #append 30 of them
l.sort()
print(l)
i=0
flag=0
while(i<len(l)-1):
    if(l[i]==l[i+1]):
        print("repeats",l[i],l[i+1])
        flag=1
        break;
    i=i+1
if (flag==0):
    print("doesn't repeat")    
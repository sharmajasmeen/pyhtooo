import random
a=22
l=[34,45,34.23,43]
for i in range(100):
    l.append(random.randint(1, 10))
flag=0
for i in range(len(l)):
    if(a==l[i]):
        print("found")
        flag=1
        break;
if (flag==0):

#     print("not found")

tu=("jass","ricky")
print(tu)



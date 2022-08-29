# import random
# l=random.sample(list(range(12000)), 1000)
# sum=0
# for i in range(len(l)):
#     sum=sum+l[i]
# print(sum)

# x=[3,4,56,44,32]
# y=[3,43,23,12,2]
# sum=0
# for i in range(len(x)):
#     sum=sum+x[i]*y[i]
# print(sum)    
def  sum_prod(a,b,c):
    ss= a+b+c
    prod=(a*b*c)
    return ss,prod
a,b,c=( float(x)for x in input("num").split())
s,p=sum_prod(a, b, c)
print(s,p)
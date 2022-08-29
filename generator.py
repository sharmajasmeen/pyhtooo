# def getNum (x):
#     if x<=1:
#         yield n
#     else:
#         yield (getNum(x-1)+getNum(x-2))
# n=int(input("terms"))
# for i in range(n):
#     print(getNum(5).__next__())
# def fibo(n):
#     a=0
#     b=1
#     yield 0
#     yield 1
#     for i in range(n):
#         p=a+b
#         a=b
#         b=p
#         yield p
# n=int(input("kuch vi"))
# get=fibo(n)
# print(get.__next__())
# print(get.__next__())
# print(get.__next__())
# print(get.__next__())
# print(get.__next__())
# print(get.__next__())
# x="89329"
# ier=iter(x)
# print(su.__next__())
# print(su.__next__())
# print(su.__next__())
# print(su.__next__())
# print(su.__next__())
def gen(x):
    for i in range(1,x):
        if i%2==0:
            yield i
n=gen(10)
print(n.__next__())
print(n.__next__())
print(n.__next__())

num=input("enter numbers")
l=[]
for i in num:
    if i.isnumeric():
      l.append(i)
      numbers=list(map(int,l))
      from functools import reduce
      z=reduce(lambda x,y:x+y,numbers)
      print("sum is",z)
    elif i.isalpha():
        print("enter only numeric")
        continue
    else:
        pass
# # from functools import lru_cache
# # @lru_cache(maxsize=16)
# # def fib(n):
# #     if n==0 or n==1:
# #         return 1
# #     else:
# #         return fib(n-1)+fib(n-2)
# # import time
# # t1=time.time()   
# # print([fib(x) for x in range(654)])
# # t2=time.time()
# # print(t2-t1)

# # ls=([i for i in range(100,200+1) if i%2==0 ])
# # print(ls)
# import numpy as np
# # a=np.array([[1,1],[3,8]])
# # print(a)
# # b=np.array([2200,10100])
# # print(b)
# # print(np.linalg.solve(a, b))
# # import datetime as datetime
# a=[10,20,10]
# b=[23,4,5]
# # c=[23,34,233,23,]
# # def dot_prod(a,b):
# #     result=0
# #     for i,j in zip(a,b):
# #        result+=i*j
# #     return result
# # import time
# # t1=time.time()    
# # for i in range(10):
# #     print(np.dot(a, b))
# # t2=time.time()
# # print("time",t2-t1)
# # import array 
# # a=array.array('i',[10,20,20,10]) #i represent int 
# # print(type(a))
# # print(a)
# # print("elements")
# # for i in a:
# #     print(i)
# # import numpy
# # a=numpy.array([10,20,30])
# # print(a)
# # for x in a:
# #     print(x)

# a=np.array([[12,22,23],[23,21,12]])
# print(a)
# print(type(a))
# print(a.ndim)
# print(a.shape) # no. of rows,no.of columns
# print(a.size)
# a=[12,"jds","ew0",2]
# a=np.array(a)
# print(a)
# a=np.array((10,23,23))
# print(a.dtype)#unicode 
# a=np.array((10,23,2.3))
# print(a.dtype)
# print(a)
# # array contains homogeneous elements if list contains heterogeneous elements
# # upcaasting will be performed.

# #why not promoted from floAT TO INT ?
# #bcz in downcASting there may be a loss of information.
# a=np.array([10,23,2.3],dtype=int)
# print(a.dtype)
# print(a)
# a=np.array([10,23,'hs'],dtype=bool) # if entity is zero it returns false for non zero it returns true
# print(a.dtype)
# print(a)
# a=np.array([10,23,0],dtype=bool) # if entity is zero it returns false for non zero it returns true
# print(a.dtype)
# print(a)

# a=np.array([10,23,0+1j],dtype=complex) # if entity is zero it returns false for non zero it returns true
# print(a.dtype)
# print(a)
# a=np.arange(1,11,3,dtype=float)
# print(a)
# a=np.linspace(0,1,7)
# print(a)
# a=np.linspace(0,1)# by default num(interval)=50
# print(a)
# a=np.linspace(0,100,10,dtype=int)
# print(a)

# def f1(a,b):
#     print(f'a vale :{a}')
#     print(f'b value :{b}')
# f1(21,2)
# f1(a=12,b=12)
# f1(10,b=12)
# f1(a=10,20) # invalid 
# #AFTER KEYWORD VALUES WE CAN'T TAKE POSITIONAL ARGUMENTS

# def f1(a,/,b):
#     print(f'a vale :{a}')
#     print(f'b value :{b}')
# f1(10,10)
# f1(a=10,b=10)#invalid
# f1(10,b=12)

def f1(a,*,b):
    print(f'a value:{a}')
    print(f' b value:{b}')
f1(10,20) #invalid
f1(10,b=20) # compulsory to take keyword argument

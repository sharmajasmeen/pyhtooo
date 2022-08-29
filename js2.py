# def check(str):
#     digit=letter=0
#     for ch in str:
#         if ch.isdigit():
#             digit=digit+1
#         elif ch.isalpha():
#             letter=letter+1
#         else:
#             pass
#     count={'math':digit,'english':letter}
#     print("No. of  Digits",count.get('math'))
#     print("No. of alphabets",count.get('english'))

# name=input("enter string")
# check(name)

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (n*fact(n-1))
# n=int(input("enter n"))
# r=int(input("enter r"))
# print(fact(n))
# print(fact(n-r))

def fact(n):
    i=1
    fact=1
    while(i<n+1):
        fact=fact*i
        i=i+1
    return fact
n=int(input("enter n"))
r=int(input("enter r"))
c=n-r
per=fact(n)/fact(c)
print(per)
com=(per)/fact(r)
print(com)

# def math(x,y):
#     sum=x+y
#     sub=x-y
#     prod=x*y
#     div=x/y
#     print("sum of numbers",sum)
#     print("subtraction of numbers",sub)
#     print("product of numbers",prod)
#     print("division of numbers",div)
# a=float(input("enter first value"))
# b=float(input("enter second value"))
# math(a,b)
# import math
# def stat(n):
#     i=1
#     sum=0
#     dev=0
#     for i in range(1,n+1):
#         a=float(input("enter number"))
#         sum=sum+a
#         dev=dev+(a*a)
#     print("sum is",sum)
#     mean=sum/n
#     print("mean is",mean)
#     var=(dev/n)-(mean*mean)
#     sd=math.sqrt(var)
#     print("variance is",var)
#     print("standard deviation is",sd)
# n=int(input("enter number of observatons"))
# stat(n)

# def fibo(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(1,n):
#         p=a+b
#         a=b
#         b=p
#         print(p)
# n=int(input("enter n"))
# fibo(n)

# def sumdigits(number):
#   if number==0:
#     return 0
#   if number!=0:
#     return (number%10)+sumdigits(number//10)
# number=int(input("Enter a number :"))
# print(sumdigits(number))

def recur_factorial(n):
   if n == 1 or n==0:
       return n
   else:
       return n*recur_factorial(n-1)

n = int(input("Enter number "))
r = int(input("Enter number "))
c=n-r
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   print("The factorial of", n, "is", recur_factorial(n))
   print("The factorial of", r, "is", recur_factorial(r))
   print("The factorial of", c ,"is", recur_factorial(c))
per=recur_factorial(n)/recur_factorial(c)
print(per)
com=(per)/recur_factorial(r)
print(com)

# file1=open("jas.txt", "r")
# text=file1.read()
# count_tab=0
# count_space=0
# count_newline=0
# no_of_character=len(text)
# for char in text:
#     if char=='\t':
#         count_tab+=1
#     if char==' ':
#         count_space+=1
#     if char=='\n':
#         count_newline+=1
# print("How many no_of_character are present in these file? ", no_of_character)
# print("How many Tabs are present in these file? ", count_tab)
# print("How many Spaces are present in these file? ", count_space)
# print("How many Newlines are present in these file? ", count_newline)
# file1.close()
# # def isPalindrome(num):
# #   rev = 0

# #   temp = num

#   while temp > 0:
#       rev = (rev*10) + (temp %10);
#       temp = temp//10

#   return rev == num

# low = int(input("Enter lower interval value \n"))
# up = int(input("Enter upper interval value \n"))
 
# print("Palindeome numbers between ",low,"and",up," are")
 
# for num in range(low,up+1):
#     if isPalindrome(num):
#       print(num)
# file1=open("numbers.txt","r")
# value=file1.read.line()
# print("max value:"+max(value))
# print("min value:"+min(value))
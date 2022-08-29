
# num=int(input("Enter a five digit number"))
# sum=0
# while(num>0):
#     dig=num%10
#     sum=sum+dig
#     num=num//10

# print("the total sum of digits is:",sum)    

# for digit in str(num):
#     sum=sum+int(digit)
# print("sum",sum)    

# BS=float(input("enter basic salary"))
# DA=0.4*BS
# HRA=0.2*BS
# GS=BS+HRA+DA
# print("The Gross salary is: "+str(GS))

# principle_amount=float(input("enter principle amount"))
# rate_of_interest=float(input("enter rate_of_interest"))
# time=float(input("enter time"))
# SI=(principle_amount*rate_of_interest*time*0.01)
# print("Simple interest is"+str(SI))
# radius=float(input("enter radius of a circle"))
# pi=3.14
# area=pi*(radius**2)
# circumference=2*pi*radius
# print("area of a circle is",str(area))
# print("circumference of a circle is",str(circumference))
# from math import sqrt
# a=float(input("enter a"))
# b=float(input("enter b"))
# c=float(input("enter c"))
# d=(b*b)-(4*a*c)
# if(d>0):
#     d1=((-b+sqrt(d))/(2*a))
#     d2=((-b-sqrt(d))/(2*a))
# print(d1,d2)

# a,b,c,d,e=(float(x) for x in input("enter five numbers").split())
# sum=a+b+c+d+e
# mean=sum/5
# print("sum is "+str(sum))
# print("average is "+str(mean))
# a,b=(float(x) for x in input("enter a and b").split())
# a,b=b,a
# print("value of a is:"+str(a))
# print("value of b is:"+str(b))

# BS=float(input("enter basic salary"))
# if(BS>=5000):
#     HRA=1000
#     DA=0.98*BS
# else:
#     HRA=0.10*BS
#     DA=0.90*BS
# GS=BS+HRA+DA
# print("The Gross salary is: "+str(GS))
# percentage=float(input("enter percentage marks"))
# if(percentage>=60):
#     print("First Division")
# elif(percentage>=50 and percentage<59):
#     print("Second Division")
# elif(percentage>=40 and percentage<49):
#     print("Third Division")
# else:
#     print("fail")
# a,b,c=(float(x) for x in input("enter first,second and third side of triangle").split())
# if a== b == c:
#     print("equilateral triangle")
# elif a==b or b==c or c==a:
#     print("isosceles triangle")
# elif (a*a+b*b==c*c or c*c+b*b==a*a or a*a+c*c==b*b):
#     print("right angled triangle")
# else:
#     print("Scalene triangle")
# for num in range(100,1000):
#   temp=num
#   sum=0
#   while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10

#   if sum==num:
#     print (num)
# 
l=int(input("enter lower range"))
u=int(input("enter upper range"))
print("The Prime Numbers in the range are: ")
for num in range(l,u+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
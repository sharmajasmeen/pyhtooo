#firstly we decide how many rows and columns we need to incorporate
#we use loops for printing  the pattern program in python no. of rows outer loop and no. of columns inner loop
#  we give the user the ability to decide the pattern size by introducing the input() function to accept the no. of rows
#iterate rows and columns .We use the for loop and range function to write the outer loop  based on no. of rows given by user 
#now to analyze the inner loop ,which depends on the value of the no. of rows specified,we use a nested loop or inner loop to specify the number columns that will go inside the outer loop

#simple pyramid
# s=int(input("no. of rows"))
# for i in range(0,s):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("")    

#reverse
# s=int(input("no. of rows"))
# for i in range(s+1,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print("")    
#equilateral
# s=int(input("no. of rows"))
# m=(2*s)-2
# for i in range(0,s):
#     for j in range(0,m):
#         print(end=" ")
#     m=m-1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print(" ")
#.....................................REverse equilateral....................
# s=int(input("no. of rows"))
# m=(2*s)-2
# for i in range(s,-1,-1):
#     for j in range(m,0,-1):
#         print(end=" ")
#     m=m+1
#     for j in range(0,i):
#         print(i,end=" ")
#     print(" ")

s=int(input("enter no. of rows"))
t=(2*s)-2
for i in range(0,s):
    for j in range(0,t):
        print(end=" ")
    t=t-1
    for j in range(0,i+1):
        print(i,end=" ")
    print("")
t=s-2
for i in range(s,-1,-1):
    for j in range(t,0,-1):
        print(end=" ")
    t=t+1
    for j in range(0,i+1):
        print(i,end=" ")
    print("")
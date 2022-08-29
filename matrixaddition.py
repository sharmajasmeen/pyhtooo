dim=2
x=[3,2]
y=[3,4]
z=[3,4]

A=[]
A.append(x)
A.append(y)
A.append(z)

x1=[3,4]
y1=[3,2]
z1=[3,3]
B=[]
B.append(x1)
B.append(y1)
B.append(z1)
print(A)
print(B)
C=[[0,0],[0,0],[0,0]]
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
          C[i][j]=C[i][j]+A[i][k]*B[k][j]

for r in C:
    print(r)

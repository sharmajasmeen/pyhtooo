#method overloading
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):

        s=0

        if a!=None and b!=None and c!=None:
           s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=student(32,34)
s2=student(34,43)
print(s1.sum(56,2))            
#method overwritting
class A:#parent class
    def show(self):
        print("nokiaa")

class B(A):#child class
    def show(self):
        print("motorola")     
a1=B()
a1.show()

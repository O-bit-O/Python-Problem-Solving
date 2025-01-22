import numpy as np
from numpy import  zeros

eq1=input("first equation: ")
eq2=input("second equation: ")
eq3=input("third equation: ")

p=eq1.split('x')
a=float(p[0])
p=p[1].split('y')
b=float(p[0])
p=p[1].split('z')
c=float(p[0])
p=p[1].split('=')
d=float(p[1])

p=eq2.split('x')
e=float(p[0])
p=p[1].split('y')
f=float(p[0])
p=p[1].split('z')
g=float(p[0])
p=p[1].split('=')
h=float(p[1])

p=eq3.split('x')
i=float(p[0])
p=p[1].split('y')
j=float(p[0])
p=p[1].split('z')
k=float(p[0])
p=p[1].split('=')
l=float(p[1])

arr1=np.array([[a,b,c],[e,f,g],[i,j,l]])
arr2=np.array([d,h,l])
y=len(arr2)
z=zeros(y,float)

for q in range(y-1):
    for r in range(q+1,y):
        fc=arr1[r,q]/arr1[q,q]
        for s in range(q,y):
            arr1[r,s]=arr1[r,s]-fc*arr1[q,s]
        arr2[r]=arr2[r]-fc*arr2[q]

z[y-1]=arr2[y-1]/arr1[y-1,y-1]
for q in range(y-2,-1,-1):
    sum=arr2[q]
    for r in range(q+1,y):
        sum=sum-arr1[q,r]*z[r]
    z[q]=sum/arr1[q,q]

print(z)
print("x=",z[0]," y=",z[1], " z=",z[2])


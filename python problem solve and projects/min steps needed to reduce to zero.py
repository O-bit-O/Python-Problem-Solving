fdata=open("input1.txt", "r")
file=open("output1.txt", "w")
a=fdata.readline().split(" ")
b=a[0]
n=int(b)
c=0
while n>0:
    m=int(max(list(str(n))))
    n=n-m
    c=c+1
file.write(str(c))
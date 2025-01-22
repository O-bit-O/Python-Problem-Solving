import math
fdata=open("input4.txt",'r')
file=open('output4.txt', 'w')
fdata=fdata.readline().split("\n")
i=0
arr=[]
while(True):
    data=fdata[i].split(" ")
    x=list(map(int,data))
    a=x[0]
    b=x[1]
    if a==0 and b==0:
        break
    else:
        count=0
        x=math.sqrt(a)
        while(x*x<=b and x*x>=a):
            count+=1
            x+=1
        arr.append(count)
    i+=1

output=""
for i in arr:
    output=output+str(i)
    output=output+"\n"
file.write(output)



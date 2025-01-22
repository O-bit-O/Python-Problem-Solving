fdata=open('input2.txt', 'r')
file=open('output2.txt', 'w')
data=[]

for i in fdata:
    data.append(i.replace('\n',''))

num=int(data[0][0])
people=int(data[0][2])
data.pop(0)
x=[]

for i in data:
    temp=i.split()
    x.append(temp)    
for i in x:
    i[0],i[1]=i[1],i[0]    
for i, j in enumerate(x):
    x[i][0]=int(j[0])
    x[i][1]=int(j[1]) 
   
x.sort()
for i in x:
    i[0],i[1]=i[1],i[0]
    
final=[]
assignment=0
y=[0]*people
c=0

for i in range(people):
    final.append(x[c])
    y[c]=final[c][1]
    c=c+1
    assignment=assignment+1
for i in range(people):
    x.pop(0)
for i in x:
    start=i[0]
    end=i[1]
    for j in range(len(y)):
        if y[j]<start:
            assignment=assignment+1
            y[j]=end
            break
 
file.write(str(assignment))
fdata=open('input3.txt', 'r')
file=open('output3.txt', 'w')
data=[]

for i in fdata:
    data.append(i.replace('\n',''))
    
work=data[1].split()
call=data[2]
work.sort()
output=""
jack=[]
jill=[]
time_J=0
time_j=0
pointer=0

for i in call:
    if i=='J':
        least=work[pointer]
        jack.append(least)
        time_J=time_J+int(least)
        output=output+least
        pointer=pointer+1
    elif i=='j':
        p=0
        temp=jack
        temp.sort(reverse=True)
        max=temp[p]
        check=True
        while check:
            if max not in jill:
                jill.append(max)
                time_j=time_j+int(max)
                output=output+max
                check=False
            else:
                p=p+1
                max=temp[p]
        
file.write(output+"\n")
file.write('Jack will work for '+str(time_J)+" hours\n")
file.write('Jill will work for '+str(time_j)+" hours\n")
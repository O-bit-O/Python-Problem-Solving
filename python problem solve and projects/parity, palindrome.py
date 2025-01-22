from asyncio.windows_events import NULL

m,n,o,p,q=0,0,0,0,0
lines=0
def parity(num):   
    if '.' in num:
        return "{} cannot have parity and ".format(float(str(num)))
    elif int(str(num))%2 == 0:
        return "{} has even parity and ".format(int(str(num)))
    else:
        return "{} has odd parity and ".format(int(str(num)))

def palindrome(word):
    if word is NULL:
        return "{} is not a palindrome".format(word)
    for i in range(0,len(word)//2):
        if word[i]!=word[len(word)-1-i]:
            return "{} is not a palindrome".format(word)
    return "{} is a palindrome".format(word)

fdata = open('input.txt','r')
fdata = fdata.read()
data=fdata.split("\n")
file = open('output1.txt','w')
for i in range(0,len(data)-1):
    lines+=1
    final_split=data[i].split(" ")
    x=parity(final_split[0])
    if " cannot have parity and " in x:
        m+=1
    elif " has even parity and " in x:
        n+=1
    else:
        o+=1
    y=palindrome(final_split[1])
    if " is not a palindrome" in y:
        p+=1
    else:
        q+=1
    file.write(x+y+"\n")

rifle = open('record.txt','w')
rifle.write("Percentage of odd parity: "+str((o/lines)*100)+"%\n")
rifle.write("Percentage of even parity: "+str((n/lines)*100)+"%\n")
rifle.write("Percentage of no parity: "+str((m/lines)*100)+"%\n")
rifle.write("Percentage of palindrome: "+str((q/lines)*100)+"%\n")
rifle.write("Percentage of non-palindrome: "+str((p/lines)*100)+"%\n")






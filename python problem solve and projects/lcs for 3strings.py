def find_max(num1, num2):
    if num1>num2:
        max=num1
    else:
        max=num2
    return max
    
def LCS(x,y,z):
    n,m,l=len(x),len(y),len(z)
    array=[[[0 for _ in range(l)] for _ in range(m)] for _ in range(n)]    
    for i in range(n):
        for j in range(m):
            for k in range(l):
                array[i][j][k]=0
                if x[i]==y[j] and x[i]==z[k]:
                    if  i>0 and j>0 and k>0:
                        v=array[i-1][j-1][k-1]+1
                    else:
                        v=1                    
                    array[i][j][k]=v                   
                else:
                    if i>0:
                        com1=array[i-1][j][k]
                    else:
                        com1=0                        
                    if j>0:
                        com2=array[i][j-1][k]
                    else:
                        com2=0                        
                    if k>0:
                        com3=array[i][j][k-1]
                    else:
                        com3=0                        
                    array[i][j][k]=find_max(find_max(com1,com2),com3)
                    
    return array[n-1][m-1][l-1]                        
        
with open("input3.txt", "r") as input:
    with open("output3.txt", "w") as output:
        lines=input.read().splitlines()
        x,y,z=map(str,lines)        
        length=LCS(x,y,z)
        output.write(str(length))
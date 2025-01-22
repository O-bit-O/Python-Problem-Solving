def quick_sort(A,p,r):
    if(p<r):
        q=partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    return A

def partition(A,p,q):
    x=A[p]
    i=p
    for j in range(p+1,q+1):
        if A[j]<=x:
            i+=1 
            A[i],A[j]=A[j],A[i]
    A[p],A[i]=A[i],A[p]
    return i

def findK(A,k):
    i=partition(A,k-1,len(A)-1)
    return A[i]

def time_complexity(array):
    x=0
    y=0
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            x+=1
        else:
            y+=1
    if x==len(array)-1 or y==len(array)-1:
        print("Time Complexity of the sort: "+"O(n^2)")  #worst case for quick_sort is when the given array is sorted=O(n^2)
    else:
        print("Time Complexity of the sort: "+"O(nlogn)")  #best and avg case=O(nlogn)

fdata = open('input5.txt','r')
fdata = fdata.read().splitlines()
data= fdata[0].split(" ")
data=[int(x) for x in data]
print(data)
time_complexity(data)

a=fdata[1:len(fdata)]
a=[int(x) for x in a]
file = open('output5.txt','w')
p=quick_sort(data, 0 , len(data)-1 )
print(p)
for i in range(len(a)):  #total time complexity=O(n^2) when it has to findk
    z=findK(p,a[i])
    file.write(str(z)+"\n")

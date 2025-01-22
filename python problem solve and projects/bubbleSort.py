#the best case for bubble sort is when the given array is already sorted
def bubbleSort(arr):
    for i in range(len(arr)-1):
        c=0
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                c=1
        if c==0:
            break
    return arr
#for the best case, the inner loop is only occurring once then breaks
#time complexity=O(n)[best case]

fdata = open('input1.txt','r')
fdata = fdata.read()
data=fdata.splitlines()[1].split()
data=[int(x) for x in data]

p=bubbleSort(data)

file = open('output1.txt','w')
for i in p:
    file.write(str(i)+" ")


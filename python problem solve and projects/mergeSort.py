def merge(array, lower, mid, upper):
    n1 = mid - lower + 1
    n2 = upper - mid    
    L = [0] * (n1)
    R = [0] * (n2)    
    for i in range(0, n1):
        L[i] = array[lower + i]       
    for j in range(0, n2):
        R[j] = array[mid + 1 + j]        
    i = 0
    j = 0
    k = lower    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1        
        k += 1        
    while  i < n1:
        array[k] = L[i]
        i += 1
        k += 1   
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1 
    return array      
        
def mergeSort(array, lower, upper):    
    if lower < upper:
        mid = (lower + upper) // 2        
        mergeSort(array, lower, mid)
        mergeSort(array, mid+1, upper)
        merge(array, lower, mid, upper)
        return array

#time complexity=O(nlogn)

fdata = open('input4.txt','r')
fdata = fdata.read().splitlines()
data= fdata[1].split(" ")
data=[int(x) for x in data]

p=mergeSort(data, 0 , len(data)-1 )
file = open('output4.txt','w')
for i in p:
    file.write(str(i)+" ")

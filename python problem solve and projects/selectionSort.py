def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if int(arr[min]) > int(arr[j]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        
    return arr

fdata = open('input2.txt','r')
fdata = fdata.read()
data=fdata.splitlines()
p=data[0].split(" ")
q=data[1].split(" ")

#p[0] has the number of elements and p[1] has the amount of data we want to write
#q is the array
#time complexity=O(n^2)

selection_sort(q)
file = open('output2.txt','w')
for i in range(int(p[1])):
    file.write(str(q[i])+" ")


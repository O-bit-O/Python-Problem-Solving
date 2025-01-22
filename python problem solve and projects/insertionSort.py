def insertion_sort(id_arr, mark_arr):
    for i in range(len(mark_arr)-1):
        temp = mark_arr[i+1]
        temp2 = id_arr[i+1]
        j = i        
        while(j >= 0):
            if mark_arr[j] < temp:
                mark_arr[j+1] = mark_arr[j]
                id_arr[j+1] = id_arr[j]
            else:
                break
        
            j -= 1
        
        mark_arr[j+1] = temp
        id_arr[j+1] = temp2
    
    return id_arr

#time complexity=O(n)[best], O(n^2)[worst,avg]

fdata = open('input3.txt','r')
fdata = fdata.read().splitlines()
p=fdata[1].split(" ")
q=fdata[2].split(" ")

r=insertion_sort(p,q)

file = open('output3.txt','w')
for i in range(len(r)):
    file.write(str(r[i])+" ")
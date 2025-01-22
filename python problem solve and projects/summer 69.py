def summer_69(arr):
    total=0
    add=True
    for i in arr:
        while add:
            if i!=6:
                total+=i
                break
            else:
                add=False
        while not add:
            if i==9:
                add=True
                break
            else:
                break
    return total



inp_arr=[1,2,9,4,6,5,6,6,7,8,9,4,6,5,5,9,5]
output_sum=summer_69(inp_arr)
print(output_sum)
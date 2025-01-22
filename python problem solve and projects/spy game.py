def spy_game(num):
    arr=[0,0,7,'abc']
    for i in num:
        if i==arr[0]:
            arr.pop(0)
    
    return len(arr)==1


inp_val=[1,2,3,0,0,5,4,6,7,8,9]
print(spy_game(inp_val))
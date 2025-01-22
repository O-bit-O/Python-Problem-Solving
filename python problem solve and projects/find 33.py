def find_33(my_list):
    for i in range(0,len(my_list)-1):
        if my_list[i] == 3 and my_list[i+1]==3:
            return True
    return False    

user_inp=input("enter numbers: ")
a=[int(i) for i in user_inp]
# a=[]
# for i in user_inp:
#     a.append(i)
print(find_33(a))
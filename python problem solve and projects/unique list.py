def unique_list(s):
    # return list(set(s))
    seen_num=[]
    for i in s:
        if i not in seen_num:
            seen_num.append(i)
    return seen_num

sample=[1,1,1,1,2,2,2,3,3,3,4,5,5,5]
print(unique_list(sample))
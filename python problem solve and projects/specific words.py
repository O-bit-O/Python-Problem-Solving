st= 'print only the words that start with S in this sentence'
a= st.split()
for i in a:
    # for j in i:          #if we needed to print the words that has "s" in them
    #     if j=='s':
    #         print(i)
    if i[0].lower()=='s':
        print(i)
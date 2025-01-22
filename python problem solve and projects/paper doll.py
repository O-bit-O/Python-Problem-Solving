def paper_doll(text):
    # a=[i for i in text]
    # b=[]
    # for i in a:
    #     b.append(i*3)
    # b=''.join(b)
    # print(b)


    # a=''
    # for i in text:
    #     a+=i*3
    # print(a)

    a=[i*3 for i in text]
    a=''.join(a)
    print(a)

inp=input("enter a string: ")
paper_doll(inp)
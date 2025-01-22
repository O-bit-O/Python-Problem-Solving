def master_yoda(inp):
    a=inp.split()
    a=a[::-1]
    print(' '.join(a))

user_inp=input("give a sentence: ")
master_yoda(user_inp)
def animal_cracker(name):
    a=name.lower().split()
    if len(a)==2:
        x=a[0]
        y=a[1]
        if x[0]==y[0]:
            print(True)
        else:
            print(False)
    else:
        print("you must enter a two-word string")


cracker_name=input("give animal cracker name: ")
animal_cracker(cracker_name)

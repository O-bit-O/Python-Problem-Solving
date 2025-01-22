def makes_twenty(a,b):
    # if a+b==20:
    #     print(True)
    # elif a==20 or b==20:
    #     print(True)
    # else:
    #     print(False)
    return (a+b)==20 or a==20 or b==20

fisrt=int(input("enter number: "))
second=int(input("enter number: "))
print(makes_twenty(fisrt,second))
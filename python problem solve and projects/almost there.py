def almost_there(num):
    print((abs(100-num))<=10 or (abs(200-num))<=10)

user_inp=int(input("enter number: "))
almost_there(user_inp)
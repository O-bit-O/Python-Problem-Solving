def other_side_of_seven(num):
    if num==7:
        print(num)
    elif num>7:
        print(7-((num-7)*2))
    else:
        print(7+((7-num)*2))


user_inp=int(input("give the number: "))
other_side_of_seven(user_inp)
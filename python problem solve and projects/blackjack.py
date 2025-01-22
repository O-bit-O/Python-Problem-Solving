def blackjack(a,b,c):
    if a+b+c<=21:
        return a+b+c
    # else:
    #     if a==11 or b==11 or c==11:
    #         i=a+b+c-10
    #         if i<=21:
    #             return i
    #         else:
    #             return 'BUST'
    #     else:
    #         return 'BUST'
    elif 11 in [a,b,c] and sum([a,b,c])<=31:
        return a+b+c-10
    else:
        return 'BUST'

first=int(input("enter a number ranging from 1 to 11: "))
second=int(input("enter a number ranging from 1 to 11: "))
third=int(input("enter a number ranging from 1 to 11: "))
print(blackjack(first,second,third))
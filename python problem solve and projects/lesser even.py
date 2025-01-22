def lesser_even(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))

first_value=int(input("give 1st number: "))
second_value=int(input("give 2nd number: "))
lesser_even(first_value,second_value)

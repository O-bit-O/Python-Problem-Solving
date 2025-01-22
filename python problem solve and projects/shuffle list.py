from random import shuffle

def shuff_list(a_list):
    shuffle(a_list)
    return a_list

def guess():
    a=''
    while a not in ['0','1','2','3']:
        a=input("enter your guess: 0 or 1 or 2 or 3 -> ")
    return int(a)
    
def checker(a_list,my_guess):
    if a_list[my_guess] == 'ABC':
        print("WOOHOO!!!")    
    else:
        print("sucks to be u")

my_list=[' ',' ','ABC',' ']

shuffled_list=shuff_list(my_list)
user_guess=guess()
checker(shuffled_list,user_guess)
print(shuffled_list)
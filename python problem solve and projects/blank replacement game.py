def choice_validation():
    x='bruh'
    while x not in [0,1,2]:
        x=input('enter position (0,1,2): ')
        if x.isdigit():
            x=int(x)
        else:
            pass
        if x not in [0,1,2]:
            print('enter a valid number')
    return x

def replacement(pos):
    user_str=input("enter your replacement string: ")
    game_list[pos]=user_str
    return game_list

def game_on():
    k='gg'
    while k not in ['y','n']:
        k=input('type y to keep playing or type n to stop: ')
        if k=='y':
            return True
        elif k=='n':
            return False
        else:
            print('enter y or n')

game_list=[' ',' ',' ']
print(game_list)
play=True
while play==True:
    x=choice_validation()
    upd_gamelist=replacement(x)
    print(upd_gamelist)
    play=game_on()



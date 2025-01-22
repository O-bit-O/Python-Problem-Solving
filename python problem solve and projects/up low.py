def up_low(str):
    # lowercase=0
    # uppercase=0

    # for i in str:
    #     if i.isupper():
    #         uppercase+=1
    #     elif i.islower():
    #         lowercase+=1
    #     else:
    #         pass
    
    # print(f'string: {str}')
    # print(f'lowercase count: {lowercase}') 
    # print(f'uppercase count: {uppercase}')

    d={'upper':0,'lower':0}

    for i in str:
        if i.isupper():
            d['upper']+=1
        if i.islower():
            d['lower']+=1
        else:
            pass

    print(f'string: {str}')
    print(f'lowercase count: {d["lower"]}') 
    print(f'uppercase count: {d["upper"]}')

s='Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
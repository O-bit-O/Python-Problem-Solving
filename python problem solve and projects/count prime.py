def count_prime(num):
    if num<2:           #convention: treat 0 and 1 as not prime
        return 0
    
    prime=[2]
    x=3
    while x<=num:
        for i in range(3,x,2):
            if x%i==0:
                x+=2
                break
        else:
            prime.append(x)
            x+=2
        
    print(prime)
    return len(prime)


inp_val=int(input("enter a number: "))
print(count_prime(inp_val))
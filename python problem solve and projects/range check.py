def range_check(num,low,high):
    if num in range(low,high+1):
        return f'{num} is within given range'
    else:
        return f'{num} is outside of range'

print(range_check(6,2,10))
def palindrome(s):
    s=s.replace(' ','')
    if s==s[::-1]:
        return 'plaindrome found'
    else:
        return 'not palindrome'

print(palindrome('nurses run'))
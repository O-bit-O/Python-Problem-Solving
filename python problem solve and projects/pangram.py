import string

def pangram(s):
    alphabet=set(string.ascii_lowercase)
    s=s.replace(' ','')
    s=s.lower()
    s=set(s)

    return s==alphabet

print(pangram('The quick brown fox jumps over the lazy dog'))
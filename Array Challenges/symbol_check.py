"""
have a string, if string contains a letter then it should
return True if letter is surrounded by '+' sign in the string
else return false.
Input: +==-+a+==-_=
Output: True
"""

def symbolcheck(strn):
    x = 'abcdefghijklmnopqrstuvwxyz'
    if strn[0] in x or strn[-1] in x:
        return False
    for i in range(1,len(strn)-1):
        if strn[i] in x:
            if strn[i-1] != '+' or  strn[i+1] != '+':
                return False
    return True

print(symbolcheck('+==+a+=='))

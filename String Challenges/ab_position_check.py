"""
 * Problem Statement                                            *
 * Have the function ABCheck(str) take the str parameter being  *
 * passed and return the string true if the characters a and b  *
 * are separated by exactly 3 places anywhere in the string at  *
 * least once (ie. "lane borrowed" would result in true because *
 * there is exactly three characters between a and b).          *
 * Otherwise return the string false.
"""

#First Solution - 
def abcheck(strn):
    a = strn.lower()
    indexofa = []
    indexofb = []
    for i in range(len(a)):
        if a[i] == 'a':
            indexofa.append(i)
        elif a[i] == 'b':
            indexofb.append(i)
    for i in indexofa:
        for j in indexofb:
            if j - i == 4:
                return True
    return False

print(abcheck("lane borrowed"))  # Output: True
print(abcheck("bdjsade"))          # Output: False

#Second Solution - 
def ABCheck(strn):
    str_lower = strn.lower()
    for i in range(len(str_lower) - 4):  # Iterate until the fourth-to-last character
        if str_lower[i] == 'a' and str_lower[i + 4] == 'b':
            return "true"
    return "false"

print(ABCheck("lane borrowed"))  # Output: true
print(ABCheck("abcde"))          # Output: false

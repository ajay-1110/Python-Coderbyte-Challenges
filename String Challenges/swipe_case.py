"""/****************************************************************
 *             CODERBYTE SWIPE CASE TWO CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function SwapII(str) take the str parameter and swap*
 * the case of each character. Then, if a letter is between two *
 * numbers (without separation), switch the places of the two   *
 * numbers.                                                     *
 * For example: if str is "6Hello4 -8World, 7 yes3"             *
 * the output should be 4hELLO6 -8wORLD, 7 YES3.                *
 *                                                              *
 * Examples                                                     *
 * Input 1: "Hello -5LOL6"                                      *
 * Output 1: hELLO -6lol5                                       *
 *                                                              *
 * Input 2: "2S 6 du5d4e"                                       *
 * Output 2: 2s 6 DU4D5E                                        *"""

def swap(strn):
    a = ""
    for i in strn:
        if i.isalpha() and i.isupper():
            a+= i.lower()
        elif i.isalpha() and i.islower():
            a += i.upper()
        else:
            a += i
    result = re.sub(r'(\d+)([a-zA-Z]+)(\d+)',r'\3\2\1',a)
    return result

print(swap("2S 6 du5d4e"))

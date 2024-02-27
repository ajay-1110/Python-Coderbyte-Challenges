"""/****************************************************************
 *             CODERBYTE LETTER CHANGES CHALLENGE               *
 *                                                              *
 * Problem Statement                                            *
 * Have the function LetterChanges(str) take the str parameter  *
 * being passed and modify it using the following algorithm.    *
 * Replace every letter in the string with the letter following *
 * it in the alphabet (ie. c becomes d, z becomes a). Then      *
 * capitalize every vowel in this new string (a, e, i, o, u)    *
 * & finally return this modified string.                       *
 *                                                              *
 * Examples                                                     *
 * Input 1: hello*3                                             *
 * Ouput 1: Ifmmp*3                                             *
 *                                                              *
 * Input 2: fun times!                                          *
 * Output 2: gvO Ujnft!                                         *"""


def letterchange(str):
    letter = "abcdefghijklmnopqrstuvwxyz"
    capital = letter.upper()
    new = ""
    for i in str:
        if i in letter:
            indx = letter.index(i)
            new_indx = (indx + 1)%26
            new += letter[new_indx]
        elif i in capital:
            indx = capital.index(i)
            new_indx = (indx + 1)%26
            new += letter[new_indx]
        else:
            new += i
    new2 = ""
    for i in new:
        if i in "aeiouAEIOU":
            new2 += i.upper()
        else:
            new2 += i
    return new2

print(letterchange("fun times!"))

"""/****************************************************************
 *             CODERBYTE CAESAR CIPHER CHALLENGE                *
 *                                                              *
 * Problem Statement                                            *
 * Have the function CaesarCipher(str,num) take the str         *
 * parameter and perform a Caesar Cipher shift on it using the  *
 * num parameter as the shifting number. A Caesar Cipher works  *
 * by shifting each letter in the string N places in the        *
 * alphabet (in this case N will be num). Punctuation, spaces,  *
 * and capitalization should remain intact.                     *
 * For example if the string is "Caesar Cipher" and num is 2    *
 * the output should be "Ecguct Ekrjgt".                        *
 *                                                              *
 * Examples                                                     *
 * Input 1: "Hello" and num = 4                                 *
 * Output 1: Lipps                                              *
 *                                                              *
 * Input 2: "abc" and num = 0                                   *
 * Output 2: abc                                                *
 *                                                              *"""

def cae(strn,num):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lettersup = letters.upper()
    x = ''
    for i in range(len(strn)):
        if strn[i] in letters:
            a = letters.index(strn[i])
            new_indx  = (a + num)%26
            x += letters[new_indx]
        elif strn[i] in lettersup:
            a = lettersup.index(strn[i])
            new_indx  = (a + num)%26
            x += lettersup[new_indx]
        else:
            x += strn[i]
    return x

print(cae("Yb i",2))

"""/****************************************************************
 *          CODERBYTE NON REPEATING CHARACTERS CHALLENGE        *
 *                                                              *
 * Problem Statement                                            *
 * Have the function NonrepeatingCharacter(str) take the str    *
 * parameter being passed, which will contain only alphabetic   *
 * characters and spaces, and return the first non-repeating    *
 * character. For example: if str is "agettkgaeee" then your    *
 * program should return k. The string will always contain at   *
 * least one character and there will always be at least one    *
 * non-repeating character.                                     *
 *                                                              *
 * Examples                                                     *
 * Input 1: "abcdef"                                            *
 * Output 1: a                                                  *
 *                                                              *
 * Input 2: "hello world hi hey"                                *
 * Output 2: w                                                  *
 *                                                              *
 ***************************************************************/"""

def nonrepeatingchar(strn):
    for i,char in enumerate(strn):
        if char not in strn[:i]+strn[i+1:]:
            return strn[i]

print(nonrepeatingchar("abcdef"))

"""/****************************************************************
 *      CODERBYTE CODELAND USERNAME VALIDATION CHALLENGE        *
 *                                                              *
 * Problem Statement                                            *
 * Have the function CodelandUsernameValidation(str) take the   *
 * str parameter being passed and determine if the string is a  *
 * valid username according to the following rules:             *
 * 1. The username is between 4 and 25 characters.              *
 * 2. It must start with a letter.                              *
 * 3. It can only contain letters, numbers, & underscore.       *
 * 4. It cannot end with an underscore character.               *
 * If the username is valid then your program should return the *
 * string true, otherwise return the string false.              *
 *                                                              *
 * Examples                                                     *
 * Input 1: "aa_"                                               *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: "u__hello_world123"                                 *
 * Output 2: true                                               *"""


import re
def username(strn):
    letters = 'qwertyuiopasdfghjklxcvbnm_'
    ul = letters.upper()
    for i in strn:
        if i not in letters and i not in ul:
            return False
        else:
            x = len(strn)
            y = ''
            if x >= 4 and x <= 25:
                for i in range(x):
                    if strn[0].isalpha():
                        if strn[-1] != "_":
                            return True
            return False
print(username('u__hello_world123'))
                    

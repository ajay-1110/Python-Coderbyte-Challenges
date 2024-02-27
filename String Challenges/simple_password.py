"""/****************************************************************
 *              CODERBYTE SIMPLE PASSWORD CHALLENGE             *
 *                                                              *
 * Problem Statement                                            *
 * Have the function SimplePassword(str) take the str parameter *
 * being passed and determine if it passes as a valid password  *
 * that follows the list of constraints:                        *
 * 1. It must have a capital letter.                            *
 * 2. It must contain at least one number.                      *
 * 3. It must contain a punctuation mark.                       *
 * 4. It cannot have the word "password" in the string.         *
 * 5. It must be longer than 7 characters and                   * 
 *    shorter than 31 characters.                               *
 * If all the above constraints are met within the string, the  *
 * your program should return the string true, otherwise your   *
 * program should return the string false.                      *
 * For example: if str is "apple!M7" then your program should   *
 * return "true".                                               *
 *                                                              *
 * Examples                                                     *
 * Input 1: "passWord123!!!!"                                   *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: "turkey90AAA="                                      *
 * Output 2: true                                               *"""

def simplepassword(strn):
    if not any(char.isupper() for char in strn):
        return 'false'
    if not any(char.isdigit() for char in strn):
        return 'false'
    if not any(char in "!@#$%^&*()_-+=[]{}\|;:<>/?\'\"" for char in strn):
        return 'false'
    if 'password' in strn.lower():
        return 'false'
    if len(strn) <= 7 or len(strn)>= 31:
        return 'false'
    return 'true'

print(simplepassword("passWord123!!!!"))  # Output: false
print(simplepassword("turkey90AAA="))     # Output: true

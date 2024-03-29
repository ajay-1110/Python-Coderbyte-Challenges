"""/****************************************************************
 *                CODERBYTE HAMMING DISTANCE CHALLENGE          *
 *                                                              *
 * Problem Statement                                            *
 * Have the function HDistance(strArr) take the array of strings*
 * stored in strArr, which will only contain two strings of     *
 * equal length and return the number of characters at each     *
 * position that are different between them.                    *
 *                                                              *
 * For example: if strArr is ["house", "hours"] then your       *
 * program should return 2. The string will always be of equal  *
 * length and will only contain lowercase characters from the   *
 * alphabet and numbers.                                        *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["10011", "10100"]                                  *
 * Output 1: 3                                                  *
 *                                                              *
 * Input 2: ["abcdef", "defabc"]                                *
 * Output 2: 6                                                  *
 *                                                              *
 ***************************************************************/"""


def hdistance(strarr):
    str1,str2 = strarr
    if len(str1) != len(str2):
        return False
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

print(hdistance(["helloworld", "worldhello"]))

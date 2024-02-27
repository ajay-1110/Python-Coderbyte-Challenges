"""/****************************************************************
 *             CODERBYTE ONE DECREMENTED CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function OneDecremented(str) count how many times a *
 * digit appears that is exactly one less than the previous     *
 * digit. For example: if str is "5655984" then your program    *
 * should return 2 because 5 appears directly after 6 and 8     *
 * appears directly after 9. The input will always contain at   *
 * least 1 digit.	                                            *
 *                                                              *
 * Examples                                                     *
 * Input 1: "56"                                                *
 * Output 1: 0                                                  *
 *                                                              *
 * Input 2: "9876541110"                                        *
 * Output 2: 6                                                  *
 *                                                              *
 ***************************************************************/"""

def onedecrement(str):
    count = 0
    if len(str) == 0 or len(str) == 1:
        return 0
    else:
        for i in range(len(str)-1):
            if int(str[i]) == int(str[i+1])+1:
                count += 1
        return count

print(onedecrement("9876541110"))

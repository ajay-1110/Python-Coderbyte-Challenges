"""/****************************************************************
 *         CODERBYTE MINIMUM WINDOW SUBSTRING CHALLENGE         *
 *                                                              *
 * Problem Statement                                            *
 * Have the function MinWindowSubstring(strArr) take the array  *
 * of strings stored in strArr, which will contain only two     *
 * strings, the first parameter being the string N and the      *
 * second parameter being a string K of some characters, and    *
 * your goal is to determine the smallest substring of N that   *
 * contains all the characters in K.                            *
 *                                                              *
 * For example: if strArr is ["aaabaaddae", "aed"] then the     *
 * smallest substring of N that contains the characters         *
 * a, e, and d is "dae" located at the end of the string.       *
 * So for this example your program should return the string    *
 *                                                              *
 * Another example: if strArr is ["aabdccdbcacd", "aad"] then   *
 * the smallest substring of N that contains all of the         *
 * characters in K is "aabd" which is located at the beginning  *
 * of the string. Both parameters will be strings ranging in    *
 * length from 1 to 50 characters and all of K's characters will*
 * exist somewhere in the string N. Both strings will only      *
 * contains lowercase alphabetic characters.                    *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["ahffaksfajeeubsne", "jefaa"]                      *
 * Output 1: aksfaje                                            *
 *                                                              *
 * Input 2: ["aaffhkksemckelloe", "fhea"]                       *
 * Output 2: affhkkse                                           *
 *                                                              *
 ***************************************************************/
"""
def min_window_substring(strArr):
    n, k = strArr[0], strArr[1]
    min_window = ""

    for i in range(len(n)):
        for j in range(i + len(k), len(n) + 1):
            window = n[i:j]
            if all(window.count(char) >= k.count(char) for char in k):
                if not min_window or len(window) < len(min_window):
                    min_window = window

    return min_window


print(min_window_substring(["aaabaaddae", "aed"])) 
print(min_window_substring(["aaffhkksemckelloe", "fhea"])) 

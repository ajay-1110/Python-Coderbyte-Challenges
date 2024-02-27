"""/****************************************************************
 *             CODERBYTE ARITHMETC GEOMETRIC II CHALLENGE       *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ArithGeo(arr) take the array of numbers    *
 * stored in arr and return the string "Arithmetic" if the      *
 * sequence follows an arithmetic pattern or return "Geometric" *
 * if it follows a geometric pattern. If the sequence doesn't   *
 * follow either pattern return -1. An arithmetic sequence is   *
 * one where the difference between each of the numbers is      *
 * consistent, where as in a geometric sequence, each term after*
 * the first is multiplied by some constant or common ratio.    *
 * Arithmetic example: [2, 4, 6, 8] and                         *
 * Geometric example: [2, 6, 18, 54]. Negative numbers may be   *
 * entered as parameters, 0 will not be entered, and no array   *
 * will contain all the same elements.                          *
 *                                                              *
 * Examples                                                     *
 * Input 1: new int[] {5,10,15}                                 *
 * Output 1: Arithmetic                                         *
 *                                                              *
 * Input 2: new int[] {2,4,16,24}                               *
 * Output 2: -1                                                 *
 *                                                              *
 ***************************************************************/"""

def ArithGeo(arr):
    if all(arr[i] - arr[i-1] == arr[1] - arr[0] for i in range(1, len(arr))) :
        return "Arithmetic"
    elif all(arr[i] / arr[i-1] == arr[1] / arr[0] for i in range(1, len(arr))) :
        return "Geometric"
    else:
        return -1

print(ArithGeo([2, 6, 18, 54]))

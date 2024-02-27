"""/****************************************************************
 *             CODERBYTE BITWISE TWO CHALLENGE                  *
 *                                                              *
 * Problem Statement                                            *
 * Have the function BitwiseTwo(strArr) take the array of       *
 * strings stored in strArr, which will only contain two        *
 * strings of equal length that represent binary numbers, and   *
 * return a final binary string that performed the              *
 * bitwise AND operation on both strings. A bitwise AND         *
 * operation places a 1 in the new string where there is a 1 in *
 * both locations in the binary strings, otherwise it places    *
 * a 0 in that spot.                                            *
 * For example: if strArr is ["10111", "01101"] then your       *
 * program should return the string "00101"                     *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["100", "000"]                                      *
 * Output 1: 000                                                *
 *                                                              *
 * Input 2: ["10100", "11100"]                                  *
 * Output 2: 10100                                              *
 *                                                              *
 ***************************************************************/"""

def bitwisetwo(arr):
    a = arr[0]
    b = arr[1]
    new = ""
    for i in range(len(a)):
        if int(a[i]) == 1 and int(b[i]) == 1:
            new += '1'
        else:
            new += '0'
    return new

print(bitwisetwo(["10100", "11100"]))

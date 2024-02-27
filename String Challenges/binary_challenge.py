"""/****************************************************************
 *               CODERBYTE OFF BINARY CHALLENGE                 *
 *                                                              *
 * Problem Statement                                            *
 * Have the function OffBinary(strArr) read the array of strings* 
 * stored in strArr, which will contain two elements, the first *
 * will be a positive decimal number and the second element will* 
 * be a binary number. Your goal is to determine how many digits* 
 * in the binary number need to be changed to represent the     *
 * decimal number correctly (either 0 change to 1 or vice versa)*
 *                                                              * 
 * For example: if strArr is ["56", "011000"] then your program *
 * should return 1 because only 1 digit needs to change in the  *
 * binary number (the first zero needs to become a 1) to        *
 * correctly represent 56 in binary.                            *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["5624", "0010111111001"]                           *
 * Output 1: 0                                                  *
 *                                                              *
 * Input 2: ["44", "111111"]                                    *
 * Output 2: 3                                                  *
 *                                                              *
 ***************************************************************/"""

def offbinary(strarr):
    a = strarr[0]
    b = "" + ''.join(i for i in sorted(strarr[1]))
    x = sorted(bin(int(a))[2:])
    y = "" + ''.join(i for i in x)
    count1 = y.count('1')
    count1inreplacement = b.count('1')
    return abs(count1 - count1inreplacement)
    
print(offbinary(["56", "011000"] ))

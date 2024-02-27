"""/****************************************************************
 *            CODERBYTE BRACKET COMBINATIONS CHALLENGE          *
 *                                                              *
 * Problem Statement                                            *
 * Have the function BracketCombinations(num) read num which    *
 * will be an integer greater than or equal to zero, and return *
 * the number of valid combinations that can be formed with num *
 * pairs of parentheses.                                        *
 *                                                              *
 * For example, if input is 3, then the possible combinations   *
 * of 3 pairs of parenthesis,                                   *
 * namely: ()()(), are ()()(), ()(()), (())(), ((())), & (()()) *
 *                                                              *
 * There are 5 total combinations when the input is 3, so your  *
 * program should return 5.                                     *
 *                                                              *
 * Examples                                                     *
 * Input 1: 3                                                   *
 * Output 1: 5                                                  *
 *                                                              *
 * Input 2: 2                                                   *
 * Output 2: 2                                                  *"""

def bracketcomb(num):
    if num == 0:
        return 1
    total_comb = 0
    for i in range(num):
        total_comb += bracketcomb(i)*bracketcomb(num - i - 1) 
    return total_comb

print(bracketcomb(3))

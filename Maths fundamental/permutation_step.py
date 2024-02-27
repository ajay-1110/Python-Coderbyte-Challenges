"""/****************************************************************
 *             CODERBYTE PERMUTATION STEP CHALLENGE             *
 *                                                              *
 * Problem Statement                                            *
 * Have the function PermutationStep(num) take the num parameter*
 * being passed & return the next number greater than num using *
 * the same digits.                                             *
 *                                                              *
 * For example: if num is 123 return 132, if it's 12453 return  *
 * 12534. If a number has no greater permutations,              *
 * return -1 (ie. 999).                                         *
 *                                                              *
 * Examples                                                     *
 * Input 1: 11121                                               *
 * Output 1: 11211                                              *
 *                                                              *
 * Input 2: 41352                                               *
 * Output 2: 41523                                              *
 *                                                              *
 * Input 3: 897654321                                           *
 * Output 3: 912345678                                          *
 *                                                              *
 * Input 4: 76666666                                            *
 * Output 4: -1                                                 *
 *                                                              *
 ***************************************************************/
"""
from itertools import permutations
def pnc(num):
    x = [''.join(c) for c in permutations(str(num),len(str(num)))]
    y =[]
    for i in x:
        y.append(int(i))
    z = set(y)
    a = sorted(z)
    final = -1
    if a[len(a)-1] == num:
        return final
    for i in range(len(a)-1):
        if a[i] == num:
            final = a[i+1]
            return final


print(pnc(11121))

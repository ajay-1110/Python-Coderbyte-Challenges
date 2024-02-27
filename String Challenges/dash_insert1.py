"""/****************************************************************
 *             CODERBYTE DASH INSERT CHALLENGE                  *
 *                                                              *
 * Problem Statement                                            *
 * Have the function DashInsert(str) insert dashes ('-')        *
 * between each two odd numbers in str. For example: if str is  *
 * 454793 the output should be 4547-9-3. Don't count zero as an *
 * odd number.                                                  *
 *                                                              *
 * Examples                                                     *
 * Input 1: 99946                                               *
 * Output 1: 9-9-946                                            *
 *                                                              *
 * Input 2: 56730                                               *
 * Output 2: 567-30                                             *
 ***************************************************************/"""

def dashinsert(strn):
    new = ''
    for i in range(len(strn)-1):
        if int(strn[i])%2 != 0 and int(strn[i+1])%2 != 0:
            new += strn[i] + '-'
        else:
            new += strn[i]
    return new + strn[-1]

print(dashinsert('9994633'))

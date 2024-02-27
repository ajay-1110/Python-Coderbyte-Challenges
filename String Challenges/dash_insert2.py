"""/****************************************************************
 *             CODERBYTE DASH INSERT TWO CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function DashInsertII(str) insert dashes ('-')      *
 * between each two odd numbers and insert asterisks ('*')      *
 * between each two even numbers in str.                        *
 *                                                              *
 * For example: if str is 4546793 the output should be          *
 * 454*67-9-3. Don't count zero as an odd or even number.       *
 *                                                              *
 * Examples                                                     *
 * Input 1: 99946                                               *
 * Output 1: 9-9-94*6                                           *
 *                                                              *
 * Input 2: 56647304                                            *
 * Output 2: 56*6*47-304                                        *
 *                                                              *
 * Solution Efficiency                                          *
 * The user scored higher than 36.2% of users who solved this   *
 * challenge.                                                   *"""

def dashinserttwo(strn):
    new = ''
    for i in range(len(strn)-1):
        if int(strn[i]) != 0 and int(strn[i + 1]) != 0:
            if int(strn[i])%2 != 0 and int(strn[i+1])%2 != 0:
                new += strn[i] + '-'
            elif int(strn[i])%2 == 0 and int(strn[i+1])%2 == 0:
                new += strn[i] + '*'
            else:
                new += strn[i]
        else:
            new += strn[i]
    return new + strn[-1]

print(dashinserttwo('56647307788809'))

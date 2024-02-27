"""/****************************************************************
 *             CODERBYTE QUESTIONS MARKS CHALLENGE              *
 *                                                              *
 * Problem Statement                                            *
 * Have the function QuestionsMarks(str) which takes the str    *
 * string parameter, which will contain single digit numbers,   *
 * letters, & question marks, & check if there are exactly 3    *
 * question marks between every pair of two numbers that add up *
 * to 10. If so, then your program should return the string     *
 * true, otherwise it should return the string false. If there  *
 * aren't any two numbers that add up to 10 in the string, then *
 * your program should return false as well.                    *
 *                                                              *
 * Test Cases                                                   *
 * For example: if str is "arrb6???4xxbl5???eee5" then your     *
 * program should return true because there are exactly 3       *
 * question marks between 6 and 4, and 3 question marks between *
 * 5 and 5 at the end of the string.                            *
 *                                                              *
 * Examples                                                     *
 * Input 1: aa6?9                                               *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: acc?7??sss?3rr1??????5                              *
 * Output 2: true                                               *
 *                                                              *
 * Input 3: 5??aaaaaaaaaaaaaaaaaaa?5?5                          *
 * Output 3: false                                              *
 *                                                              *
 * Input 4: 9???1???9???1???9                                   *
 * Output 4: true                                               *
 *                                                              *"""

def questionmarks(str):
    numbers = "0123456789"
    if len(str) < 5:
        return False
    else:
        for i in range(len(str)-4):
            if str[i] in numbers and str[i+4] in numbers:
                if int(str[i]) + int(str[i+4]) == 10:
                    que = "???"
                    check = ""
                    for j in range(i+1,i+4):
                        check += str[j]
                    if check == que:
                        return True
        return False
    
print(questionmarks("9???1???89??87656"))

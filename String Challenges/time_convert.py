"""/****************************************************************
 *             CODERBYTE TIME CONVERT CHALLENGE                 *
 *                                                              *
 * Problem Statement                                            *
 * Have the function TimeConvert(num) take the num parameter    *
 * being passed and return the number of hours and minutes the  *
 * parameter converts to (ie. if num = 63 then the output       *
 * should be 1:3). Separate the number of hours and minutes     *
 * with a colon.                                                *
 *                                                              *
 * Examples                                                     *
 * Input 1: 126                                                 *
 * Output 1: 2:6                                                *
 *                                                              *
 * Input 2: 45                                                  *
 * Output 2: 0:45                                               *"""

def timeconvert(num):
    hour = num//60
    minutes = num - (hour*60)
    time = str(hour) + ':' + str(minutes)
    return time

print(timeconvert(45))

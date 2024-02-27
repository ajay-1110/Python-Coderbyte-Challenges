"""
 *             CODERBYTE COUNTING MINUTES ONE CHALLENGE         *
 *                                                              *
 * Problem Statement                                            *
 * Have the function CountingMinutesI(str) take the str         *
 * parameter being passed which will be two times               *
 * (each properly formatted with a colon and am or pm)          *
 * separated by a hyphen and return the total number of minutes *
 * between the two times. The time will be in a 12 hour clock   *
 * format.                                                      * 
 * For example: if str is 9:00am-10:00am then the               *
 * output should be 60. If str is 1:00pm-11:00am the output     *
 * should be 1320.                                              *
 *                                                              *
 * Examples                                                     *
 * Input 1: "12:30pm-12:00am"                                   *
 * Output 1: 690                                                *
 *                                                              *
 * Input 2: "1:23am-1:08am"                                     *
 * Output 2: 1425                                               *
"""

def countminutes(strn):
    start_strn , end_strn = strn.split('-')
    
    start_hour, start_min = start_strn[:-2].split(':')  
    end_hour, end_min = end_strn[:-2].split(':')  
    start_ampm = start_strn[-2:]
    end_ampm = end_strn[-2:]
    start_hour = int(start_hour)
    start_min = int(start_min)
    end_hour = int(end_hour)
    end_min = int(end_min)

    if start_ampm == 'pm':
        start_hour = start_hour + 12 if start_hour != 12 else 12
    else:
        start_hour = start_hour if start_hour != 12 else 0
    
    if end_ampm == 'pm':
        end_hour = end_hour + 12 if end_hour != 12 else 12
    else:
        end_hour = end_hour if end_hour != 12 else 0
        
    start_min = 60 * start_hour + start_min
    end_min = 60 * end_hour + end_min
    
    if start_min <= end_min:
        return end_min - start_min
    else:
        return 24 * 60 - start_min + end_min
    

print(countminutes("10:00am-11:00pm"))

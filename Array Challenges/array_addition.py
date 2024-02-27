"""/****************************************************************
 *             CODERBYTE ARRAY ADDITION I CHALLENGE             *
 *                                                              *
 * Problem Statement                                            *
 * Have the function ArrayAdditionI(arr) take the array of      *
 * numbers stored in arr and return the string true if any      *
 * combination of numbers in the array (excluding the largest   *
 * number) can be added up to equal the largest number in the   *
 * array, otherwise return the string false.                    *
 * For example: if arr contains [4, 6, 23, 10, 1, 3] the output *
 * should return true because 4 + 6 + 10 + 3 = 23. The array    *
 * will not be empty, will not contain all the same elements,   *
 * and may contain negative numbers.                            *
 *                                                              *
 * Examples                                                     *
 * Input 1: [5,7,16,1,2]                                        *
 * Output 1: false                                              *
 *                                                              *
 * Input 2: [3,5,-1,8,12]                                       *
 * Output 2: true                                               *
 *                                                              *
 ***************************************************************/"""

from itertools import combinations as c
def arrayaddition(arr):
    arr.sort()
    maxnum = arr[-1]
    arr.pop(-1)
    combo = []
    for i in range(1,len(arr)+1):
        for j in c(arr,i):
            combo.append(j)
    if maxnum in (sum(sumnum) for sumnum in combo):
        return 'True'
    else:
        return 'False'
    
print(arrayaddition([3,5,-1,8,12]))

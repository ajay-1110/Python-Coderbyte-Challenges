"""/****************************************************************
 *              CODERBYTE CONSECUTIVE CHALLENGE                 *
 *                                                              *
 * Problem Statement                                            *
 * Have the function Consecutive(arr) take the array of integers*
 * stored in arr and return the minimum number of integers      *
 * needed to make the contents of arr consecutive from the      *
 * lowest number to the highest number. For example: If arr     *
 * contains [4, 8, 6] then the output should be 2 because two   *
 * numbers need to be added to the array (5 and 7) to make it a *
 * consecutive array of numbers from 4 to 8.                    *
 * Negative numbers may be entered as parameters and no array   *
 * will have less than 2 elements.                              *
 *                                                              *
 * Examples                                                     *
 * Input 1: [5,10,15] 		                                *
 * Output 1: 8                                                  *
 *                                                              *
 * Input 2: [-2,10,4]                                           *
 * Output 2: 10                                                 *
 *                                                              *
 ***************************************************************/"""
def consecutive(arr):
    x = len(arr)
    arr.sort()
    y = []
    for i in range(arr[0],arr[-1]+1):
        y.append(i)
    return abs(len(y) - x)

print(consecutive([-2,10,4]))
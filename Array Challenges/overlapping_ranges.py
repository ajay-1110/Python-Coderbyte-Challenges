"""/****************************************************************
 *             CODERBYTE OVERLAPPING RANGES CHALLENGE           *
 *                                                              *
 * Problem Statement                                            *
 * Have the function OverlappingRanges(arr) take the array of   *
 * numbers stored in arr which will contain 5 positive integers,*
 * the first two representing a range of numbers (a to b), the  *
 * next 2 also representing another range of integers (c to d), *
 * and a final 5th element (x) which will also be a positive    *
 * integer, and return the string true if both sets of ranges   *
 * overlap by at least x numbers.                               *
 * For example: if arr is [4, 10, 2, 6, 3] then your program    *
 * should return the string true.                               *
 * The first range of numbers are 4, 5, 6, 7, 8, 9, 10 & the    *
 * second range of numbers are 2, 3, 4, 5, 6.                   *
 * The last element in the array is 3, and there are 3 numbers  *
 * that overlap between both ranges: 4, 5, and 6.               *
 * If both ranges do not overlap by at least x numbers,         *
 * then your program should return the string false.            *
 *                                                              *
 * Examples                                                     *
 * Input 1: [5,11,1,5,1]                                        *
 * Output 1: true                                               *
 *                                                              *
 * Input 2: [1,8,2,4,4]                                         *
 * Output 2: false                                              *
 *                                                              *
 ***************************************************************/"""
def overlappingranges(arr):
    first_range = arr[:2]
    second_range = arr[2:4]
    overlap = arr[-1]
    first_numbers = []
    for i in range(first_range[0],first_range[1] + 1):
        first_numbers.append(i)
    second_numbers = []
    for j in range(second_range[0],second_range[1] + 1):
        second_numbers.append(j)
    count = 0
    if len(first_numbers) >= len(second_numbers):
        for i in second_numbers:
            if i in first_numbers:
                count += 1
    elif len(first_numbers) <= len(second_numbers):
        for i in first_numbers:
            if i in second_numbers:
                count += 1
    if count == overlap:
        return True
    return False

print(overlappingranges([1,8,2,4,4]))

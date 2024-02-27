"""/****************************************************************
 *                 CODERBYTE MAX SUBARRAY CHALLENGE             *
 *                                                              *
 * Problem Statement                                            *
 * Have the function MaxSubarray(arr) take the array of numbers *
 * stored in arr and determine the largest sum that can be      *
 * formed by any contiguous subarray in the array.              *
 * For example, if arr is [-2, 5, -1, 7, -3] then your program  *
 * should return 11 because the sum is formed by the subarray   *
 * [5, -1, 7]. Adding any element before or after this subarray *
 * would make the sum smaller.                                  *
 *                                                              *
 * Examples                                                     *
 * Input 1: [1, -2, 0, 3]                                       *
 * Output 1: 3                                                  *
 *                                                              *
 * Input 2: [3, -1, -1, 4, 3, -1]                               *
 * Output 2: 8                                                  *
 *                                                              *
 ***************************************************************/"""

from itertools import combinations
def find_contiguous_subarrays(arr):
    subarrays = []
    n = len(arr)
    for i, j in combinations(range(n + 1), 2):
        subarrays.append(arr[i:j])
    sum1 = []
    for i in subarrays:
        sum1.append(sum(i))
    return max(sum1)

print(find_contiguous_subarrays([3, -1, -1, 4, 3, -1]))

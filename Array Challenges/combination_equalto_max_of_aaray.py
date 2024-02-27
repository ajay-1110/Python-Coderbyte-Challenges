#array addition equals to max
#any combinations of array equal to max of array after removing max of array

from itertools import combinations
def ArrayAdditionI(arr):
    arr.sort()
    largest = arr[-1]
    for r in range(1, len(arr)):
        for combo in combinations(arr[:-1], r):
            if sum(combo) == largest:
                return True
    return False

arr = [4, 6, 23, 2, 25, 3]
result = ArrayAdditionI(arr)
print(result) 

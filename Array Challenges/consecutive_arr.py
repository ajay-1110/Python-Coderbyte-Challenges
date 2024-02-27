# Using the Python language, have the function Consecutive(arr) take the array of integers stored in arr and return the
# minimum number of integers needed to make the contents of arr consecutive from the lowest number to the highest
# number. For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the
#  array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as parameters
# and no array will have less than 2 elements.

def cons(arr):
    x = sorted(arr)
    min_ = x[0]
    max_ = x[-1]
    numbers_required = (max_ - min_)-1 
    counter = 0
    for i in range(min_ + 1, max_):
        if i in x:
            counter = 0
        else :
            counter += 1
    output = numbers_required - counter
    return output

print(cons([-1,2,4]))

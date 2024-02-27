"""              Tripple Double Challenge 
* Have the function TripleDouble(num1,num2) take both parameters being passed,    *
* and return 1 if there is a straight triple of a number at any place in num1     *
* and also a straight double of the same number in num2.                          *
* For example: if num1 equals 451999277 and num2 equals 41177722899,              *
* then return 1 because in the first parameter you have the straight triple 999   * 
* and you have a straight double, 99, of the same number in the second parameter. * 
* If this isn't the case, return 0.                                               *
"""
#2nd solution has easy approach than 1st solution.

#First solution -
def trippledouble(num1,num2):
    num1str = str(num1)
    num2str = str(num2)
    x = []
    y = []
    for i in set(num1str):
        x.append(i*3)
    for i in set(num2str):
        y.append(i*2)
    for i in x:
        for j in y:
            if i[0] == j[0]:
                if i in num1str and j in num2str:
                    return True
    return False

print(trippledouble(8288738393999377,339397349977744223))


#Second solution - 
def triple_and_double(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    for digit in range(10):
        triple_str = str(digit) * 3
        double_str = str(digit) * 2
        if triple_str in num1_str and double_str in num2_str:
            return 1
    return 0
 
num1 = 451999277
num2 = 41177722899
result = triple_and_double(num1, num2)
print(result)
